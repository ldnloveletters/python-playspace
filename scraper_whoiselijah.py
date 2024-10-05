from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Safari WebDriver
driver = webdriver.Safari()

# Open the website
driver.get('https://whoiselijah.com.au/collections/scents')

# Wait for the products to be loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//li[@class='grid__item']")))

# Print the page source to verify the content is loaded
print(driver.page_source)

# Find all product containers using XPath
products = driver.find_elements(By.XPATH, "//li[@class='grid__item']")

# Print the number of products found
print(f"Number of products found: {len(products)}")

# Loop through the products and extract the relevant information
for product in products:
    try:
        # Extract the name using XPath
        name = product.find_element(By.XPATH, ".//a[@class='full-unstyled-link']").text
        price = product.find_element(By.XPATH, ".//span[@class='price']").text
        print(f'Product: {name}, Price: {price}')
    except Exception as e:
        print(f"Couldn't retrieve product data for this item: {e}")

# Close the browser
driver.quit()
