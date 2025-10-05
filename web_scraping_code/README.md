# 🕸️ Product Scraper

A **Python web scraper** built with `requests` and `BeautifulSoup` that extracts product details (name, price, and link) from paginated e-commerce pages and saves them into a clean, structured CSV file.

## 🚀 Features

✅ Fetches multiple product listing pages automatically

✅ Parses product name, price, and link from each page

✅ Includes retry logic with delays to handle connection issues

✅ Logs progress and errors using Python’s built-in `logging` module

✅ Exports results to a CSV file (`products.csv`)

## 🧩 Technologies Used

🐍 Python 3.x

- 🌐 Requests – for making HTTP requests
- 🍲 BeautifulSoup4 – for parsing HTML
- 🧾 CSV – for structured data export
- ⏱️ Time – for delays between retries
- 🧠 Logging – for progress tracking

## 📦 Installation

1. Clone this repository
```bash
git clone https://github.com/yourusername/product-scraper.git
cd product-scraper
```

2. Install dependencies
```bash
pip install requests beautifulsoup4
````
## ⚙️ Usage

1. Update the `BASE_URL` in the script:
```python
BASE_URL = "https://example.com/products?page="
```

2. Adjust CSS selectors in  `parse_products()` based on the target website’s HTML:
```python
for item in soup.select(".product-card"):
    name = item.select_one(".product-title").get_text(strip=True)
    price = item.select_one(".product-price").get_text(strip=True)
    link = item.select_one("a")["href"]
```

3. Run the scraper
```
python scraper.py
```

4. Check your output
   
A file named `products.csv` will be created in your project folder containing:
```
name,price,link
Product 1,$10.99,https://example.com/product1
Product 2,$15.49,https://example.com/product2
```
## 🛠️ Configuration

You can modify scraping parameters in the main section:
```
scraped_data = scrape_all_pages(start=1, end=3)
```
- `start`: Starting page number
- `end`: Ending page number

## ⚡ Example Logging Output

```pgsql
2025-10-05 10:30:22 - INFO - Fetching URL: https://example.com/products?page=1
2025-10-05 10:30:23 - INFO - Found 12 products on page 1
2025-10-05 10:30:25 - INFO - Saved 36 items to products.csv
```

## 📄 Output Example (CSV)

| name      | price  | link                                                         |
| --------- | ------ | ------------------------------------------------------------ |
| Product 1 | ₹999   | [https://example.com/product1](https://example.com/product1) |
| Product 2 | ₹1,299 | [https://example.com/product2](https://example.com/product2) |
| Product 3 | ₹1,899 | [https://example.com/product3](https://example.com/product3) |

## ⚠️ Disclaimer

***This script is for educational and ethical use only.
Always ensure you comply with the target website’s robots.txt and Terms of Service before scraping.***

## 🧑‍💻 Author

**Mantra Patil**

📧 techmantrapatil@gmail.com
