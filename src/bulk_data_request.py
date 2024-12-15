"""
This script fetches bulk data\'s metadata from the Scryfall API and saves it to a local file.
Modules:
    requests: To make HTTP requests to the Scryfall API.
    os: To interact with the operating system, such as creating directories and file paths.
    json: To handle JSON data.
Constants:
    CACHE_DIR (str): Directory to store cached data.
    BULK_DATA_PATH (str): Path to the bulk-data.json file.
    SCRYFALL_BULK_DATA_URL (str): URL to the Scryfall bulk data endpoint.
    HEADERS (dict): Required headers to send with the request.
    TIMEOUT (int): Timeout for the request in seconds.
    FORCE (bool): Whether to force writing to file even if file already exists.
Functions:
    make_api_request(url, params=None, headers=None, timeout=10):
        Makes a GET request to the specified URL with optional parameters and headers.
    get_bulk_data(force=False):
        Get the Scryfall bulk data metadata and save it to a file.
Usage:
    Run this script directly to fetch and save the Scryfall bulk data.

Returns:
    None
"""

# Import necessary libraries
import os
import json
import requests

# Constants
CACHE_DIR = "../data/cache"
BULK_DATA_PATH = os.path.join(CACHE_DIR, "bulk-data.json")
SCRYFALL_BULK_DATA_URL = "https://api.scryfall.com/bulk-data"
HEADERS = {
    "user-agent": "EXUBERANTEXPLORER/0.0.1",
    "Accept": "application/json"
}
TIMEOUT = 10
FORCE = False

def make_api_request(url, params=None, headers=None,timeout=10):
    """
    Makes a GET request to the specified URL with optional parameters and headers.

    :param url: The URL to make the request to.
    :param params: (Optional) Dictionary of query string parameters.
    :param headers: (Optional) Dictionary of HTTP headers.
    :return: Response object from the request.
    """
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_bulk_data(force=False):
    """Get the Scryfall bulk data metadata and save it to a file.

    Args:
        force (bool, optional): Whether you'd like to force write the file. Defaults to False.
    """
    # Check if the cache directory exists, if not create it
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    # Check if the bulk-data.json file exists, if not create it
    if not os.path.exists(BULK_DATA_PATH) or force:
        # Make the request
        response = make_api_request(SCRYFALL_BULK_DATA_URL, headers=HEADERS, timeout=TIMEOUT)
        if response:
            print("Response: ", response.status_code)

            # Save the response to a file
            with open(BULK_DATA_PATH, "w", encoding = "utf-8") as f:
                json.dump(response.json(), f)
                print("Bulk data saved to file.")

# Get Scryfall bulk data
if __name__ == "__main__":
    get_bulk_data(force=FORCE)
