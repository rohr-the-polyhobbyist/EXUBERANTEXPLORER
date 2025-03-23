# EXUBERANTEXPLORER

## Project Overview

EXUBERANTEXPLORER is a project of education and fun. In this project, I will learn to use web APIs and do some ML on Magic: The Gathering (MTG) cards. While I don't have any intention to turn this project into a web application, that could be something I eventually like to do as well! Some ideas and checkpoints I hope to achieve:  
  
- Successfully connect with Scryfall's Web API to get MTG card data  
- Do something fun and basic with this data  
- Successfully web scrape some MTG commander format data from another source  
- Do something fun and basic with this data

I've decided to separate the functions I develop for this project into my `tithe_extractor` package: https://github.com/rohr-the-polyhobbyist/tithe-extractor. This project repo will include primarily jupyter notebooks and python scripts to request, store, clean, process, and visualize MTG card data. Eventually, it'd be cool to be able to make deckbuilding recommendations, but for now that goal is far off!

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rohr-the-polyhobbyist/EXUBERANTEXPLORER.git
    ```

2. Navigate to the project directory:

    ```bash
    cd EXUBERANTEXPLORER
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
  * I've been actually exploring using [`uv` by astral](https://docs.astral.sh/uv/) as I learn git CI/CD and other practices. I'm not exactly sure what options are available for others, but this package should have the files necessary to `uv run` the necessary scripts and to install package dependencies with uv. (I could be wrong on that)  

## Usage

~~This section is under revision as I settle on a project structure that makes sense. Currently, I am looking to replicate [this project structure](https://gist.github.com/ericmjl/27e50331f24db3e8f957d1fe7bbbe510?permalink_comment_id=5031342) to get started.~~  
I will need to update this section - for now, the quick description:
- `uv run scripts/get_scryfall_bulk_metadata.py` to download the metadata from Scryfall's API
- You can got through the **explore-bulk-card-data** notebook to download the oracle card data and start to explore it. (in prog.)

## Contributing

I am not currently accepting contributions to the project.  
Feel free to fork the repository to start on your own code based on this project!  

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
