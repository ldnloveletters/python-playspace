import requests
from bs4 import BeautifulSoup

# URL of the website
url = 'https://whoiselijah.com.au/collections/scents'

# Send a request to fetch the HTML content of the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the product elements (check the correct structure using inspect element)
    products = soup.find_all('div', class_='grid-product__content')

    # Loop through each product and extract the name and price
    for product in products:
        # Error handling in case the element is not found
        name_tag = product.find('a', class_='full-unstyled-link')
        price_tag = product.find('span', class_='price')

        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            print(f'Product: {name}, Price: {price}')
        else:
            print('Product data not found for this item')
else:
    print('Failed to retrieve the webpage')
