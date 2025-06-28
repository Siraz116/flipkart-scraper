# backend/config.py

import os
from dotenv import load_dotenv

# Try to load .env file if it exists
try:
    load_dotenv()
except:
    pass

# MySQL configuration (loaded from .env or use defaults)
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "flipkart_scraper")
}

# Scraper settings
BASE_URL = "https://www.flipkart.com"
SEARCH_KEYWORD = "smartphone"       # You can change this
MAX_PAGES = 3

