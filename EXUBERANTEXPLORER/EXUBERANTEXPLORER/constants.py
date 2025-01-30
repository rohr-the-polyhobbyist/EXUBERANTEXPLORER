"""This file contains constants used in the project."""
import os

# Constants
cwd = os.getcwd()
PROJECT_DIR = cwd + "/EXUBERANTEXPLORER/EXUBERANTEXPLORER/EXUBERANTEXPLORER"
CACHE_DIR = cwd + "EXUBERANTEXPLORER/data/cache"
BULK_METADATA_PATH = cwd + "EXUBERANTEXPLORER/data/cache/bulk-data.json"
SCRYFALL_BULK_DATA_URL = "https://api.scryfall.com/bulk-data"
HEADERS = {"user-agent": "EXUBERANTEXPLORER/0.1.0", "Accept": "application/json"}
TIMEOUT = 10
FORCE = False
