# mets (MetroSearch)

mets is a command-line interface (CLI) tool for searching and retrieving data from the Metropolitan Museum of Art's public API.

## User Documentation


### Features

- Search by title or tags only
- Optional JSON output
- Ascending / descending sort order by objectBeginDate
- Asynchronous image downloading
- Customizable image download path
- Progress bar for downloads


### Installation

1. Clone the repository and build the package:
   ```bash
   git clone https://gitlab.com/cgs2824870/mets.git
   cd mets
   pip install .
   ```

### Usage

```bash
python -m mets <search_term> [options]
```

#### Options:

- `-i`, `--images`: Only return objects with images. Default: True
- `-n`, `--num`: Maximum number of results to return. Default: 80
- `-s`, `--sort`: Sort results by date (0: ascending, 1: descending, other: no sort). Default: 0
- `-o`, `--output`: Output JSON filename. Prints to stdout if not provided.
- `-m`, `--time`: Delay between API requests in seconds. Default: 0.001
- `-d`, `--download`: Download object images
- `-p`, `--path`: Folder to save downloaded images. Default: 'images'
- `-t`, `--title`: Search in title only
- `-g`, `--tags`: Search in tags only


#### Defaults:

- Search performed by classification string by default
- Only search for objects with images
- Maximum number of objects to return is 80
- Sort results by date ascending
- Images are NOT downloaded by default
- Default images output folder is 'images'

#### Example

```bash
python -m mets paintings
python -m mets sunflower -o out -d
```

This searches for objects containing "sunflower", returns up to 5 results sorted by date descending, saves the output to `out.json`, and downloads the associated images.

## Developer Documentation

### Project Structure

```
mets/
├── src/
│   └── mets/
│       ├── __init__.py
│       └── mets.py
├── tests/
│   └── test_mets.py
├── pyproject.toml
└── README.md
```

### Architecture

mets consists of two main classes:

1. `MetroSearch`: Handles API interactions with the Metropolitan Museum.
2. `MetroCLI`: Manages the command-line interface and user interactions.

### API Endpoints

- Search: `https://collectionapi.metmuseum.org/public/collection/v1/search`
- Object details: `https://collectionapi.metmuseum.org/public/collection/v1/objects/[objectID]`

### Dependencies

- httpx: For making HTTP requests
- argparse: For parsing command-line arguments
- asyncio: For asynchronous operations
- aiofiles: For asynchronous file operations
- tqdm: For progress bars

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://gitlab.com/cgs2824870/mets.git
   cd mets
   ```

2. Install the package in editable mode with development dependencies:
   ```bash
   pip install -e .[test]
   ```

3. Run tests:
   ```bash
   pytest
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
