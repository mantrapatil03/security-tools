import requests
from bs4 import BeautifulSoup
import csv
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom headers to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/116.0.0.0 Safari/537.36'
}

# Base URL (example)
BASE_URL = "https://example.com/products?page="


def fetch_page(url, retries=3, delay=2):
    """
    Fetch HTML content from a URL with retry logic.
    """
    for attempt in range(retries):
        try:
            logging.info(f"Fetching URL: {url}")
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                return response.text
            else:
                logging.warning(f"Non-200 status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
        time.sleep(delay)
    return None


def parse_products(html):
    """
    Parse HTML content using BeautifulSoup to extract product data.
    """
    soup = BeautifulSoup(html, "html.parser")
    products = []

    # Modify this according to the website structure
    for item in soup.select(".product-card"):
        name = item.select_one(".product-title").get_text(strip=True)
        price = item.select_one(".product-price").get_text(strip=True)
        link = item.select_one("a")["href"]

        products.append({
            "name": name,
            "price": price,
            "link": link
        })

    return products


def scrape_all_pages(start=1, end=5):
    """
    Scrape multiple pages (paginated).
    """
    all_products = []
    for page_num in range(start, end + 1):
        url = BASE_URL + str(page_num)
        html = fetch_page(url)
        if html:
            products = parse_products(html)
            if products:
                logging.info(f"Found {len(products)} products on page {page_num}")
                all_products.extend(products)
            else:
                logging.info(f"No products found on page {page_num}")
        else:
            logging.warning(f"Skipping page {page_num} due to errors.")
    return all_products


def save_to_csv(data, filename="products.csv"):
    """
    Save scraped data to CSV.
    """
    if not data:
        logging.warning("No data to save.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    logging.info(f"Saved {len(data)} items to {filename}")


# Main script execution
if __name__ == "__main__":
    scraped_data = scrape_all_pages(start=1, end=3)  # scrape 3 pages as example
    save_to_csv(scraped_data)

