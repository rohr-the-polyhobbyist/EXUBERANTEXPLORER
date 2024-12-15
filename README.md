# EXUBERANTEXPLORER

## Project Overview

EXUBERANTEXPLORER is a project of education and fun. In this project, I will learn to use web APIs, possibly some web scraping, and eventually, some ML. While I don't have any intention to turn this project into a web application, that could be something I eventually like to do as well! Some ideas and checkpoints I hope to achieve:  
  
- Successfully connect with Scryfall's Web API to get MTG card data  
- Do something fun and basic with this data  
- Successfully web scrape some MTG commander format data from another source  
- Do something fun and basic with this data

## Features

- Pull Magic: The Gathering card data from Scryfall web API
  - Uses `requests` for HTTP requests
- ~~Web scraping of Magic: The Gathering card data~~
  - ~~Uses `BeautifulSoup` for parsing HTML~~
- ~~Data processing and analysis using embedding techniques~~
  - ~~Uses `numpy` for numerical operations~~
  - ~~Uses `scikit-learn` for machine learning algorithms~~

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/<yourusername>/EXUBERANTEXPLORER.git
    ```

2. Navigate to the project directory:

    ```bash
    cd EXUBERANTEXPLORER
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

From the project directory, follow the following instructions to use different features.  
  
1. Collect the metadata for Scryfall's bulk data:

    ```bash
    cd src
    python -m bulk_data_request.py
    ```

## Contributing

I am not currently accepting contributions to the project.  
Feel free to fork the repository to start on your own code based on this project!  

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
