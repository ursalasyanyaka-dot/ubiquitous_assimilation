import requests
from bs4 import BeautifulSoup

# step 1: Get the HTML target URL
url = "https://books.toscrape.com"

# step 2: Send a GET request to the URL
response = requests.get(url)
if response.status_code == 200:
    # step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # step 4: Find all book titles and prices
    titles = soup.find_all('h3')
    prices = soup.find_all('p', class_='price_color')

    # step 5: Display results
    for title, price in zip(titles, prices):
        print(f'"{title.get_text()}" - {price.get_text()}')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")