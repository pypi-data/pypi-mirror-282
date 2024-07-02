
"""
Copyright (c) 2024 Alex Khalyavin
This file is part of mets, released under the MIT License.
"""

import unittest
from unittest.mock import MagicMock, patch

from mets import MetroCLI, MetroSearch


class TestMetroSearch(unittest.TestCase):
	@patch("mets.MetroSearch.client")
	def test_search(self, mock_client):
		# Mock the HTTP response
		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.json.return_value = {"objectIDs": [1, 2, 3]}
		mock_client.return_value.get.return_value = mock_response
		# Call the search method
		result = MetroSearch.search("test")
		# Assert the result
		self.assertEqual(result, [1, 2, 3])

	@patch("mets.MetroSearch.client")
	def test_retrieve(self, mock_client):
		# Mock the HTTP response
		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.json.return_value = {"objectID": 1, "title": "Test Object", "objectBeginDate": 2000}
		mock_client.return_value.get.return_value = mock_response
		# Call the retrieve method
		result = MetroSearch.retrieve([1])
		# Assert the result
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0]["title"], "Test Object")


class TestMetroCLI(unittest.TestCase):
	@patch("mets.MetroSearch.search")
	@patch("mets.MetroSearch.retrieve")
	@patch("mets.MetroSearch.download")
	def test_search_cli(self, mock_download, mock_retrieve, mock_search):
		# Mock the search and retrieve methods
		mock_search.return_value = [1, 2, 3]
		mock_retrieve.return_value = [{"objectID": 1, "title": "Test Object"}]
		# Create a mock args object
		args = MagicMock()
		args.term = "test"
		args.images = True
		args.num = 1
		args.sort = 0
		args.output = None
		args.download = False
		args.title = False
		args.tags = False
		args.time = 0.001
		# Call the search method
		MetroCLI.search(args)
		# Assert that the methods were called with correct arguments
		mock_search.assert_called_once_with(term="test", img=True, mode=0)
		mock_retrieve.assert_called_once_with([1, 2, 3], max_num=1, sort=0, delay=0.001)


if __name__ == "__main__":
	unittest.main()
