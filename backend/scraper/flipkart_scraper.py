# backend/scraper/flipkart_scraper.py

from urllib.parse import quote_plus
import time

class FlipkartScraper:
    def __init__(self, browser, parser, base_url, keyword, max_pages=3):
        self.browser = browser
        self.parser = parser
        self.base_url = base_url
        self.keyword = keyword
        self.max_pages = max_pages

    def scrape(self):
        all_products = []
        encoded_keyword = quote_plus(self.keyword)

        for page in range(1, self.max_pages + 1):
            print(f"[INFO] Scraping page {page}...")

            url = f"{self.base_url}/search?q={encoded_keyword}&page={page}"
            html = self.browser.get_page(url)
            products = self.parser.parse_products(html)

            print(f"[INFO] Page {page} → {len(products)} products found.")
            all_products.extend(products)
            time.sleep(2)

        return all_products
