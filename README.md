# Web Crawler for Product Data Extraction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9.3-green)
![Pandas](https://img.shields.io/badge/Pandas-1.2.4-yellow)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.5.2-purple)

## Overview

This project involves the development of a web crawler using Python that automates the process of gathering product data from [this e-commerce website](https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=). Additionally, a web application using Flask is built to display the collected product data. This project provides a foundation for automating data collection tasks and can be extended to suit various use cases in e-commerce, market research, and data analysis.

## Features

- **Automated Web Crawling**: Iterates over multiple pages of the website to gather product information.
- **Data Extraction**: Sends HTTP GET requests to the website, parses the HTML content using BeautifulSoup, and extracts relevant details.
- **Data Storage**: Extracted data is stored in a list of dictionaries.
- **Web Application**: Flask app defines a route ('/') to render a template for displaying extracted data.

## Project Workflow

1. **Initialization**
2. **Web Crawling**
3. **Data Processing**
4. **Flask Integration**
5. **Web Application Deployment**

## Technologies Used

- **Python**: Core programming language for web crawling and backend development.
- **Flask**: Web framework for building the web application.
- **BeautifulSoup**: Library for parsing HTML and extracting data.
- **Pandas**: Data manipulation and analysis library.
- **HTML**: Markup language for creating web pages.
- **Bootstrap**: Front-end framework for designing responsive web pages.

## Setup and Installation

**Clone the repository:**
   ```sh
   git clone https://github.com/Kanch-prog/web-crawler-product-data.git
   cd web-crawler-product-data
Create a virtual environment:

sh
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install dependencies:

sh
Copy code
pip install -r requirements.txt
Run the web crawler:

sh
Copy code
python web_crawler.py
Run the Flask application:

sh
Copy code
python app.py
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:5000/
Usage
The web crawler will extract product data from the specified URL and store it.
The Flask application will display the extracted data in a web interface.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

vbnet
Copy code

This README file uses labels to indicate the technologies used, and provides clear and concis

 ![image1](https://github.com/Kanch-prog/Crawler/assets/121807277/52034987-cb7e-4a74-a3ea-6ad39c6f255a)
![image2](https://github.com/Kanch-prog/Crawler/assets/121807277/ea7d0ebb-40ff-40a7-8edc-1dfab28d95d9)


	
