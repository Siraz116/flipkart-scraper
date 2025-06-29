# backend/main.py

from config import DB_CONFIG, BASE_URL, SEARCH_KEYWORD, MAX_PAGES
from scraper.browser import Browser
from scraper.parser import Parser
from scraper.flipkart_scraper import FlipkartScraper
from db.database import MySQLDatabase
import sys

def main():
    print(f"[INFO] Starting Flipkart scraper for keyword: '{SEARCH_KEYWORD}'")
    print(f"[INFO] Target pages: {MAX_PAGES}")
    print(f"[INFO] Base URL: {BASE_URL}")

    try:
        # Initialize database and create table
        print("[INFO] Initializing database...")
        db = MySQLDatabase(DB_CONFIG)
        db.create_table()

        # Set up browser and parser
        print("[INFO] Setting up browser...")
        browser = Browser(headless=True)
        parser = Parser()
        scraper = FlipkartScraper(browser, parser, BASE_URL, SEARCH_KEYWORD, MAX_PAGES)

        # Scrape and store data
        print("[INFO] Starting scraping process...")
        products = scraper.scrape()
        print(f"[INFO] Found {len(products)} products total.")


        
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
        print("[ERROR] Please check:")
        print("  1. MySQL server is running")
        print("  2. Database credentials are correct")
        print("  3. Chrome and ChromeDriver are installed")
        print("  4. Internet connection is available")
        sys.exit(1)
    
    finally:
        # Cleanup
        try:
            if 'db' in locals():
                db.close()
            if 'browser' in locals():
                browser.quit()
        except:
            pass
        
        print("[SUCCESS] Data scraping and saving completed.")

if __name__ == "__main__":
    main()
