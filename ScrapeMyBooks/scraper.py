import requests
from bs4 import BeautifulSoup
import csv

# URL of the page we want to scrape
url = "http://books.toscrape.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all book items
books = soup.find_all('article', class_='product_pod')

# Create a CSV file to save the data
with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Title', 'Price'])

    # Extract book titles and prices and write to CSV
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        writer.writerow([title, price])

print("Data has been saved to scraped_data.csv")
