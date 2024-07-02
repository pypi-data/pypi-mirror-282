#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Metropolitan Museum of Art API Search Tool
This script provides a command-line interface for searching and retrieving data from the Metropolitan Museum of Art's public API.

Copyright (c) 2024 Alex Khalyavin
This file is part of mets, released under the MIT License.
"""

__author__ = "Alex Khalyavin"
__email__ = "soluwell3@gmail.com"

import argparse
import asyncio
import inspect
import json
import logging
import time
import sys
from pathlib import Path
from typing import List
from urllib.parse import urlencode


if not logging.getLogger().hasHandlers():
	fmt = '%(asctime)s - "%(name)s" (%(filename)s:%(lineno)d), %(levelname)s\t:"%(message)s"'
	logging.basicConfig(level=logging.INFO, format=fmt)
CFL = Path(inspect.getsourcefile(lambda: 0)).resolve()
CWD = CFL.parent
LOG = logging.getLogger(CFL.stem)

# Third-party deps
import aiofiles
import httpx
from tqdm.asyncio import tqdm as atqdm


# Patch httpx logging level
logging.getLogger("httpx").setLevel(logging.WARNING)



class MetroSearch:
	"""Handle interactions with the Metropolitan Museum of Art API."""

	search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
	obj_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

	@staticmethod
	def client():
		"""
		Create an HTTP client.

		Returns:
			httpx.Client: An instance of httpx Client.
		"""
		return httpx.Client()

	@staticmethod
	def search(term="sunflowers", img=True, mode=0):
		"""
		Search for objects using Metro REST API.

		Args:
			term (str): The search term. Defaults to "sunflowers".
			img (bool): If True, only return objects with images. Defaults to True.
			mode (int): The search mode. 0 to search everywhere, 1 for title only, 2 for tags only. Defaults to 0.

		Returns:
			List[int]: A list of object IDs matching the search criteria.
		"""
		client = MetroSearch.client()
		params = []
		if mode == 0:
			params.append(("q", ''))
			params.append(("classification", term))
		elif mode == 1:
			params.append(("title", "true"))
			params.append(("q", term))
		elif mode == 2:
			params.append(("tags", "true"))
			params.append(("q", term))
		if img:
			params.append(("hasImages", "true"))
		url = f"{MetroSearch.search_url}?{urlencode(params)}"
		response = client.get(url)
		if response.status_code == 200:
			data = response.json()
			oids = data.get("objectIDs", [])
			res = oids
		else:
			res = []
		client.close()
		return res

	@staticmethod
	def retrieve(oids: List[int], max_num=80, sort=0, delay=0.001) -> List:
		"""
		Retrieve given Object IDs data from Metro API.

		Args:
			oids (List[int]): A list of object IDs to retrieve.
			max_num (int): The maximum number of objects to retrieve. Defaults to 80.
			sort (int): The sorting order. 0 for ascending, 1 for descending. Defaults to 0.
			delay (float): The delay between API requests in seconds. Defaults to 0.001.

		Returns:
			List[dict]: A list of dictionaries containing object details.
		"""
		client = MetroSearch.client()
		res = []
		oids = oids or []
		max_retries = 3
		for oid in oids:
			obj_url = f"{MetroSearch.obj_url}{oid}"
			for attempt in range(max_retries):
				try:
					response = client.get(obj_url)
					response.raise_for_status()
					data = response.json()
					res.append(data)
					break
				except httpx.HTTPStatusError as e:
					if e.response.status_code == 429:
						LOG.info(f"Rate limit hit for object {oid}. Retrying in {delay} seconds...")
						time.sleep(delay)
						delay += 0.01
					else:
						break
				except Exception as e:
					LOG.info(f"An error occurred for object {oid}: {e}")
					break
			if len(res) >= max_num:
				break
			time.sleep(delay)
		client.close()
		if sort == 0:
			res = sorted(res, key=lambda x: x["objectBeginDate"])
		elif sort == 1:
			res = sorted(res, key=lambda x: x["objectBeginDate"], reverse=True)
		return res

	@staticmethod
	async def get_img(client, url, fpn):
		"""
		Download an image from the given URL and save it to the specified path.

		Args:
			client (httpx.AsyncClient): Async client for the HTTP request.
			url (str): Image URL
			fpn (str): Destination file path.

		Returns:
			bool: True if the download was successful, False otherwise.
		"""
		async with client.stream('GET', url) as response:
			if response.status_code == 200:
				async with aiofiles.open(fpn, 'wb') as f:
					async for chunk in response.aiter_bytes():
						await f.write(chunk)
				return True
		return False

	@staticmethod
	async def download_async(json_data, dst, batch_size=20):
		"""
		Download object images in batches.
		On large number of files API bugs out, we need to split large number of files

		Args:
			json_data (List[dict]): Objects as JSON data
			dst (str or Path): Destination folder
			batch_size (int): batch size

		Returns:
			List[bool]: A list of boolean values indicating the success status of each download.
		"""
		dst = Path(dst)
		dst.mkdir(parents=True, exist_ok=True)

		# Gather tasks from all objects
		tasks = []
		for obj in json_data:
			oid = obj['objectID']
			dst_dir = dst / str(oid)
			dst_dir.mkdir(parents=True, exist_ok=True)
			images = [obj.get('primaryImage')] if obj.get('primaryImage') else []
			images.extend(obj.get('additionalImages', []))
			for i, img_url in enumerate(images):
				if img_url:
					fname = f"image_{i + 1}.jpg"
					fpn = dst_dir / fname
					tasks.append((img_url, str(fpn)))

		# Download images in batches
		res = []
		sz = len(tasks)
		async with httpx.AsyncClient() as client:
			progress = atqdm(total=sz, desc="Downloading images")
			for i in range(0, sz, batch_size):
				batch = tasks[i:i+batch_size]
				batch_tasks = [MetroSearch.get_img(client, url, fpn) for url, fpn in batch]
				batch_results = await asyncio.gather(*batch_tasks)
				res.extend(batch_results)
				progress.update(len(batch))
				await asyncio.sleep(0.01)  # Small delay between batches
			progress.close()
		successful = sum(res)
		LOG.info(f"Images downloaded to {dst.absolute()}. Successful: {successful}, Failed: {sz - successful}")
		return res

	@staticmethod
	def download(json_data, dst, batch_size=20):
		"""
		Download images for the retrieved objects using async function.

		Args:
			json_data (List[dict]): Objects JSON data
			dst (str or Path): Destination folder.
			batch_size (int): Batch size
		"""
		asyncio.run(MetroSearch.download_async(json_data, dst, batch_size))

	@staticmethod
	def test():
		"""
		Simple test method

		This method searches for "paintings", retrieves up to 5 results, and logs the results.
		"""
		oids = MetroSearch.search(term="paintings", img=True, mode=0)
		res = MetroSearch.retrieve(oids, max_num=5)
		LOG.info(res)



class MetroCLI:
	"""Command-line interface using MetroSearch backend."""

	@staticmethod
	def search(args):
		"""
		Main search function

		Args:
			args (argparse.Namespace): Parsed args
		"""
		mode = 0
		if args.title:
			mode = 1
		elif args.tags:
			mode = 2
		oids = MetroSearch.search(term=args.term, img=args.images, mode=mode)
		res = MetroSearch.retrieve(oids, max_num=args.num, sort=args.sort, delay=args.time)
		json_data = json.dumps(res, indent=2)
		if args.output:
			if not args.output.lower().endswith(".json"):
				args.output += ".json"
			with open(args.output, "w") as ouf:
				ouf.write(json_data)
			LOG.info(f"{len(res)} objects written to {args.output}")
		else:
			print(json_data)
		# Download
		if args.download:
			if not args.path:
				args.path = CWD / "images"
			MetroSearch.download(res, args.path)

	@staticmethod
	def setup():
		"""
		Set up the command-line argument parser.

		Returns:
			argparse.ArgumentParser: A configured argument parser.
		"""
		parser = argparse.ArgumentParser(description="Metro CLI")
		parser.add_argument("term", help="Search term")
		parser.add_argument("-i", "--images", action="store_true", default=True, help="Only return objects with images, default = True")
		parser.add_argument("-n", "--num", type=int, default=80, help="Maximum number of results to return, default = 10")
		parser.add_argument("-s", "--sort", type=int, default=0, help="Sorting: By date ascending (0), By date descending (1), any other value (no sort), default = 0 (ascending)")
		parser.add_argument("-o", "--output", nargs='?', const='out', type=str, help="Writes out.json file with search results. Optionally can be used to set the filename.")
		parser.add_argument("-m", "--time", type=float, default=0.001, help="Delay between requests, default = 0.001 seconds")
		parser.add_argument("-d", "--download", action="store_true", default=False, help="Download all images.")
		parser.add_argument("-p", "--path", type=str, default="images", help="Folder to save downloaded images, default = 'images'")
		parser.add_argument("-t", "--title", action="store_true", default=False, help="Search in title only. Off by default.")
		parser.add_argument("-g", "--tags", action="store_true", default=False, help="Search in tags only. Off by default.")
		return parser

	@classmethod
	def run(cls):
		"""
		Set up the argparser, parse the arguments, execute the search.

		"""
		parser = cls.setup()
		if len(sys.argv) == 1:
			parser.print_help()
			sys.exit(1)
		args = parser.parse_args()
		cls.search(args)



def main():
	"""
	Main entry point for the app.

	This function calls the MetroCLI.run() method to start the CLI application.
	"""
	MetroCLI.run()



if __name__ == "__main__":
	main()
