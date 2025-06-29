# backend/scraper/test_scraper.py

import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import BASE_URL, SEARCH_KEYWORD, MAX_PAGES
from browser import Browser
from parser import Parser
from flipkart_scraper import FlipkartScraper

def test_scraper():
    """Test the scraper without database operations"""
    
    print(f"[TEST] Testing scraper for keyword: '{SEARCH_KEYWORD}'")
    print(f"[TEST] Target pages: {MAX_PAGES}")
    
    try:
        # Set up browser and parser
        print("[TEST] Setting up browser...")
        browser = Browser(headless=False)  # Set to False for debugging
        parser = Parser()
        scraper = FlipkartScraper(browser, parser, BASE_URL, SEARCH_KEYWORD, MAX_PAGES)

        # Test scraping
        print("[TEST] Starting scraping test...")
        products = scraper.scrape()
        
        print(f"\n[TEST] Results:")
        print(f"Total products found: {len(products)}")
        
        if products:
            print(f"\n[TEST] Sample products:")
            for i, product in enumerate(products[:5], 1):  # Show first 5 products
                print(f"\n{i}. Title: {product['title'][:100]}...")
                print(f"   Price: ₹{product['price']}")
                print(f"   Image: {product['image_url'][:50]}...")
        else:
            print("[TEST] No products found!")
            print("[TEST] This might indicate:")
            print("  1. Website structure has changed")
            print("  2. Network connectivity issues")
            print("  3. Search keyword returned no results")

    
    except Exception as e:
        print(f"[ERROR] Test failed: {e}")
        print("[ERROR] Please check:")
        print("  1. Chrome and ChromeDriver are installed")
        print("  2. Internet connection is available")
        print("  3. Flipkart website is accessible")
    
    finally:
        # Cleanup
        try:
            if 'browser' in locals():
                browser.quit()
        except:
            pass
        
        print("\n[TEST] Test completed.")

if __name__ == "__main__":
    test_scraper() 