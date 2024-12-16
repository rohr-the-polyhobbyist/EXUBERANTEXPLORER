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
    get_bulk_data_metadata(force=False):
        Get the Scryfall bulk data metadata and save it to a file.
Usage:
    Run this script directly to fetch and save the Scryfall bulk data.

Returns:
    None
"""
from EXUBERANTEXPLORER.EXUBERANTEXPLORER.constants import CACHE_DIR, BULK_DATA_PATH, SCRYFALL_BULK_DATA_URL, HEADERS, TIMEOUT, FORCE

def make_api_request(url, params=None, headers=None, timeout=10):
    """
    Makes a GET request to the specified URL with optional parameters and headers.

    :param url: The URL to make the request to.
    :param params: (Optional) Dictionary of query string parameters.
    :param headers: (Optional) Dictionary of HTTP headers.
    :return: Response object from the request.
    """
    import requests
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def get_bulk_data_metadata(force=False):
    """Get the Scryfall bulk data metadata and save it to a file.

    Args:
        force (bool, optional): Whether you'd like to force write the file. Defaults to False.
    """
    import os
    import json

    # Check if the cache directory exists, if not create it
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    # Check if the bulk-data.json file exists, if not create it
    if not os.path.exists(BULK_DATA_PATH) or force:
        # Make the request
        response = make_api_request(
            SCRYFALL_BULK_DATA_URL, headers=HEADERS, timeout=TIMEOUT
        )
        if response.status_code == 200:
            print("Request successful.")

            # Save the response to a file
            with open(BULK_DATA_PATH, "w+", encoding="utf-8") as f:
                json.dump(response.json(), f)
                print("Bulk data saved to file.")
                return response.json()
        elif response.status_code == 404:
            print(
                "Something went wrong. The requested resource was not found. Error 404."
            )
        elif response.status_code == 429:
            print("Rate limit exceeded. Please wait and try again later.")
        elif response.status_code == 503:
            print("Service unavailable. Please try again later.")
        elif response.status_code.startswith("5"):
            print("Server error. Please try again later.")
        elif response.status_code.startswith("4"):
            print("Client error. Please check the request and try again.")
    else:
        bulk_data_metadata = json.load(open(BULK_DATA_PATH, "r", encoding="utf-8"))
        return bulk_data_metadata

def get_bulk_data_info(card_type="oracle_cards"):
    """Get the Scryfall bulk data metadata for the card type(s) provided.

    Args:
        card_type (str or list): The bulk data type to retrieve. Defaults to "oracle_cards".

    Returns:
        bulk_data_info (dict): The bulk data information.
            If card_type is a string, returns a dictionary.
            If card_type is a list, returns a dictionary of dictionaries.
    """
    import os
    import json

    # Error check the card_type variable
    if not os.path.exists(BULK_DATA_PATH):
        raise FileNotFoundError("Bulk data metadata does not exist.")
    if not isinstance(card_type, list) and not isinstance(card_type, str):
        raise TypeError("card_type must be a string or list of strings.")
    if isinstance(card_type, list):
        for element in card_type:
            if not isinstance(element, str):
                raise TypeError("Elements in card_type must be strings.")
    # Load the bulk data metadata
    with open(BULK_DATA_PATH, "r", encoding="utf-8") as f:
        bulk_data = json.load(f)

    # Check to see if the card type is in the bulk data metadata
    if isinstance(card_type, str):
        for meta_data in bulk_data["data"]:
            if meta_data["type"] == card_type:
                return meta_data
    else:
        bulk_data_info = {}
        for element in card_type:
            for meta_data in bulk_data["data"]:
                if meta_data["type"] == element:
                    bulk_data_info[element] = meta_data
        return bulk_data_info

def get_bulk_data_gzip():
    """Get the Scryfall bulk data and save it to a file.

    Args:
        url (str): The URL to make the request to.
        path (str): The path to save the file to.
        force (bool, optional): Whether you'd like to force write the file. Defaults to False.

    Returns:
        response (response.request): The response object from the request.
    """
    # Empty function to be implemented later
    return None
