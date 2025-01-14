# YouTube Scraper

This script is used to scrape YouTube search results for a given keyword and extract the channel names and subscriber counts. It utilizes the Selenium library to automate web browsing and the Pandas library to store the data in an Excel file.

## Prerequisites

- Python 3.x
- Selenium library
- Pandas library
- Chrome WebDriver

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install the required libraries by running the following command:
    ```
    pip install selenium pandas
    ```
3. Download the Chrome WebDriver from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Extract the WebDriver executable and add its location to the system's PATH environment variable.

## Usage

1. Run the script using the following command:
    ```
    python script.py
    ```
2. Enter the search keyword when prompted.
3. Enter the number of times to scroll the page when prompted.
4. The script will scrape the YouTube search results and save the channel names and subscriber counts in an Excel file named `<search_keyword>_youtube_channels.xlsx`.

Note: Make sure to have a stable internet connection while running the script.

## License

This project is licensed under the [MIT License](LICENSE).
