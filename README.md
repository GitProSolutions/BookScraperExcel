#BookScraperExcel

## Project Description

This project is a web scraper built in Python that is capable of scraping book data from Amazon.com. It uses the `requests`, `beautifulsoup4`, and `pandas` libraries, as well as the `random` and `time` modules, to make HTTP requests, parse HTML content, and export the data to an Excel file. 

The web scraper is enhanced with the ability to handle blocks and use multiple proxies, which makes it more reliable and efficient. It also sets up an application programming interface (API) using the `API` class, which allows users to retrieve the book data in a convenient format (as a list of dictionaries), and export the data to an Excel file for further analysis or use.

## Table of Contents

1. [How to Install and Run the Project](#how-to-install-and-run-the-project)
2. [How to Use the Project](#how-to-use-the-project)
3. [Credits](#credits)
4. [License](#license)
5. [Badges](#badges)

## How to Install and Run the Project

1. Clone the repository: `git clone https://github.com/GitProSolutions/BookScraperExcel.git`.
2. Install the required dependencies by running `pip install -r requirements.txt` in the project directory.
3. Run the `main.py` file in a Python environment with the required dependencies installed.

## How to Use the Project

1. In the `main.py` file, modify the `BASE_URL` variable to the Amazon search results page of your choice.
2. Modify the `num_pages` variable to the number of pages of results you want to scrape.
3. If desired, modify the `API_KEY` and `API_SECRET` variables to your own values.
4. Run the `main.py` file and wait for the book data to be scraped and exported to an Excel file.
5. To use the API, make a GET request to the following URL: `http://localhost:5000/api/v1/books?key=YOUR_API_KEY`. Replace `YOUR_API_KEY` with the `API_KEY` variable value in the `main.py` file.

## Credits

This project was built by GitProSolutions as a learning exercise in web scraping, API development, and Python programming. 

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Badges

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
