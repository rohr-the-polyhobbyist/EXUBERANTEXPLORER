'''
This script pulls the bulk data metadata from the Scryfall API and saves it to the data directory.
'''
# Import functions and constants from EXUBERANTEXPLORER package
from EXUBERANTEXPLORER.custom_functions import make_api_request, get_bulk_data_metadata, get_bulk_data_info
from EXUBERANTEXPLORER.constants import SCRYFALL_BULK_DATA_URL, HEADERS, TIMEOUT, FORCE

print(SCRYFALL_BULK_DATA_URL)
# Make a request to the Scryfall bulk data endpoint
response = make_api_request(SCRYFALL_BULK_DATA_URL, headers=HEADERS, timeout=TIMEOUT)

# Save the bulk data metadata to a file
bulk_data_metadata = get_bulk_data_metadata(force=True)

# Get the bulk data information - will select oracle cards by default
bulk_data_info = get_bulk_data_info(card_type="oracle_cards")

# Print the bulk data information
print(bulk_data_info)