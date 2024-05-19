#developed a web crawler using Python to gather product data from manufacturer websites or online catalogs. The goal was to automate the process of collecting product information, such as product names, descriptions, prices, and specifications.
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def crawl_manufacturer_website(manufacturer_url):
    # Initialize empty list to store product data
    product_data = []
    
    # Iterate over multiple pages if applicable
    for page_number in range(1, 4):  # Assuming there are 3 pages
        # Send HTTP GET request to the manufacturer website
        response = requests.get(f"{manufacturer_url}{page_number}")
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find product elements on the page
            product_elements = soup.find_all('div', class_='thumbnail')
            
            # Extract product information
            for product_element in product_elements:
                # Extract product details such as name, price, description, etc.
                product_name = product_element.find('a', class_='title').text.strip()
                product_price = product_element.find('h4', class_='price').text.strip()
                product_description = product_element.find('p', class_='description').text.strip()
                product_link = urljoin(manufacturer_url, product_element.find('a', class_='title')['href'])
                
                # Add product data to list
                product_data.append({
                    'name': product_name,
                    'price': product_price,
                    'description': product_description,
                    'link': product_link
                })
        else:
            # failed request, print error message
            print(f"Error: Unable to fetch data from page {page_number} of the manufacturer website.")

    return product_data

manufacturer_url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page='
product_data = crawl_manufacturer_website(manufacturer_url)

# Convert product data to DataFrame for further processing
product_df = pd.DataFrame(product_data)

# Display extracted product data
#print(product_df)
# Initialize Flask app
app = Flask(__name__)
# Route to display product data
@app.route('/')
def display_product_data():
    return render_template('product_data.html', product_df=product_df)

# App Run
if __name__ == '__main__':
    app.run(debug=True)