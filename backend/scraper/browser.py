# backend/scraper/browser.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class Browser:
    def __init__(self, headless=True):
        options = Options()
        if headless:
            options.add_argument("--headless=new")  # for Chrome 109+
        
        # Anti-detection settings
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        try:
            # Try to use local chromedriver.exe first
            if os.path.exists("chromedriver.exe"):
                print("[INFO] Using local chromedriver.exe")
                service = Service(executable_path="chromedriver.exe")
                self.driver = webdriver.Chrome(service=service, options=options)
            else:
                # Fallback to PATH
                print("[INFO] Using ChromeDriver from PATH")
                self.driver = webdriver.Chrome(options=options)
            
            # Execute script to remove webdriver property
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            print("[BROWSER] Chrome browser initialized successfully")
        except Exception as e:
            print(f"[ERROR] Failed to initialize Chrome browser: {e}")
            print("[INFO] Make sure Chrome and ChromeDriver are installed")
            print("[INFO] Either:")
            print("  1. Place chromedriver.exe in the project root directory, or")
            print("  2. Add ChromeDriver to your system PATH")
            raise

    def get_page(self, url):
        try:
            print(f"[BROWSER] Loading URL: {url}")
            self.driver.get(url)
            
            # Wait for page to load
            time.sleep(5)
            
            # Wait for product cards to appear
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='_1AtVbE'], div[class*='_2kHMtA'], div[class*='_1xHGtK']"))
                )
            except:
                print("[WARN] Product cards not found, continuing anyway...")
            
            # Scroll down to load more content
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            return self.driver.page_source
        except Exception as e:
            print(f"[ERROR] Failed to load page {url}: {e}")
            return ""

    def quit(self):
        
        if hasattr(self, 'driver'):
            self.driver.quit()
            print("[BROWSER] Browser closed")
