# Flipkart Product Scraper

A Python-based web scraper for extracting product information from Flipkart, one of India's largest e-commerce platforms. This project follows Object-Oriented Programming principles and implements clean, scalable code architecture.

## Features

- **Multi-page Scraping**: Scrapes up to 3 pages of search results
- **Product Data Extraction**: Collects title, price, and image URL for each product
- **Database Storage**: Stores data in MySQL database for further analysis
- **Anti-Detection**: Implements measures to avoid bot detection
- **Error Handling**: Robust error handling and logging
- **Configurable**: Easy configuration through environment variables

## Technology Stack

- **Python 3.x**
- **Selenium WebDriver** - For browser automation
- **BeautifulSoup4** - For HTML parsing
- **MySQL** - Database storage
- **python-dotenv** - Environment variable management

## Project Structure

```
flipkart-scraper/
├── backend/
│   ├── main.py                 # Main execution script
│   ├── config.py               # Configuration settings
│   ├── db/
│   │   ├── database.py         # Database operations
│   │   ├── view_database.py    # Database viewer utility
│   │   └── clear_database.py   # Database clearing utility
│   └── scraper/
│       ├── browser.py          # Browser setup and management
│       ├── parser.py           # HTML parsing logic
│       ├── flipkart_scraper.py # Main scraper class
│       └── test_scraper.py     # Test scraper functionality
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Prerequisites

1. **Python 3.9+**
2. **MySQL Server** (running locally or remotely)
3. **Google Chrome** browser
4. **ChromeDriver** (compatible with your Chrome version)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd flipkart-scraper
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install ChromeDriver

#### Windows:
<!-- 1. Download ChromeDriver from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/) --> 
1. Download ChromeDriver from [https://developer.chrome.com/docs/chromedriver/downloads](https://developer.chrome.com/docs/chromedriver/downloads)

   Downloaded ChromeDriver link : [https://storage.googleapis.com/chrome-for-testing-public/138.0.7204.0/win64/chromedriver-win64.zip](https://storage.googleapis.com/chrome-for-testing-public/138.0.7204.0/win64/chromedriver-win64.zip)
   
   My Chrome Version : `138.0.7204.50 (Official Build) (64-bit)`

3. Extract and place `chromedriver.exe` in your system PATH or project directory
(put `chromedriver.exe` here: `..\flipkart-scraper\chromedriver.exe`)


### 5. Database Setup

1. **Create MySQL Database:**
```sql
CREATE DATABASE flipkart_scraper;
```

2. **Configure Database Connection:**
- Create a `.env` file in the `backend/` directory:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=flipkart_scraper
   ```
   

## Usage

### Basic Usage

1. **Navigate to the backend directory:**
```bash
cd backend
```

2. **Run the scraper:**
```bash
python main.py
```
The scraper will automatically create the database table if it doesn't exist.

3. **View database contents:**
```bash
python db/view_database.py
```

### Debugging Utilities

The project includes several debugging tools to help troubleshoot issues:

1. **Test Scraper (without database):**
```bash
cd backend/scraper
python test_scraper.py
```
This tests the scraper functionality without saving to database, useful for debugging scraping issues.

2. **View Database:**
```bash
cd backend
python db/view_database.py
```
Shows all scraped data in a formatted table view.

3. **Clear Database:**
```bash
cd backend
python db/clear_database.py
```
Clears all scraped data from the database. Useful for starting fresh or removing old data.

### Configuration

You can modify the following settings in `config.py` or through environment variables:

- `SEARCH_KEYWORD`: Product to search for (default: "smartphone")
- `MAX_PAGES`: Number of pages to scrape (default: 3)
- `DB_HOST`: MySQL host (default: localhost)
- `DB_USER`: MySQL username (default: root)
- `DB_PASSWORD`: MySQL password (default: empty)
- `DB_NAME`: Database name (default: flipkart_scraper)

### Example Output

```
[INFO] Starting Flipkart scraper for keyword: 'smartphone'
[INFO] Target pages: 3
[INFO] Base URL: https://www.flipkart.com
[INFO] Initializing database...
[DB] Connected to MySQL successfully.
[DB] Table 'product_info' ensured.
[INFO] Setting up browser...
[BROWSER] Chrome browser initialized successfully
[INFO] Starting scraping process...
[BROWSER] Loading URL: https://www.flipkart.com/search?q=smartphone&page=1
[DEBUG] Found 24 product cards
[INFO] Page 1 → 24 products found.
...
[SUCCESS] Successfully stored 72/72 products in database.
[SUCCESS] Data scraping and saving completed.
```
