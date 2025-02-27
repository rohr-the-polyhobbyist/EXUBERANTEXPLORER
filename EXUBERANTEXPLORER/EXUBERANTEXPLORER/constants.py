"""This file contains constants used in the project."""
import os

# Constants
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
sp_dir = os.path.split(MODULE_DIR)[0]
PROJECT_DIR = os.path.split(sp_dir)[0]
DATA_DIR = os.path.join(PROJECT_DIR, "data")
CACHE_DIR = os.path.join(DATA_DIR, "cache")
BULK_METADATA_PATH = os.path.join(CACHE_DIR, "bulk-data.json")
SCRYFALL_BULK_DATA_URL = "https://api.scryfall.com/bulk-data"
HEADERS = {"user-agent": "EXUBERANTEXPLORER/1.0.0", "Accept": "application/json"}
TIMEOUT = 10
FORCE = False