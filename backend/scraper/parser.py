# backend/scraper/parser.py

from bs4 import BeautifulSoup
import re

class Parser:
    def parse_products(self, html):
        soup = BeautifulSoup(html, "html.parser")
        
        # Updated selectors based on actual Flipkart HTML structure
        product_cards = []
        
        # Try the actual Flipkart product card selector
        card_selectors = [
            "div[class*='_75nlfW']",  # Main product container
            "div[class*='tUxRFH']",   # Product card wrapper
            "div[data-id]",           # Any div with data-id (product identifier)
        ]
        
        for selector in card_selectors:
            cards = soup.select(selector)
            if cards:
                product_cards = cards
                print(f"[DEBUG] Found {len(cards)} cards using selector: {selector}")
                break
        
        # Fallback: look for any div with product-like attributes
        if not product_cards:
            product_cards = soup.find_all("div", {"data-id": re.compile(r".*")})
            print(f"[DEBUG] Found {len(product_cards)} cards using data-id fallback")
        
        # Final fallback: look for any div with class containing product indicators
        if not product_cards:
            all_divs = soup.find_all("div", class_=re.compile(r".*"))
            product_cards = [div for div in all_divs if any(keyword in str(div.get('class', '')) for keyword in ['_75', '_tU', 'data-id'])]
            print(f"[DEBUG] Found {len(product_cards)} cards using generic fallback")

        items = []
        print(f"[DEBUG] Processing {len(product_cards)} product cards")
        
        for i, card in enumerate(product_cards):
            try:
                # Try multiple selectors for title
                title = self.extract_title(card)
                
                # Try multiple selectors for price
                price = self.extract_price_from_card(card)
                
                # Try multiple selectors for image
                image_url = self.extract_image_url(card)
                
                if title and price and image_url:
                    items.append({
                        "title": title,
                        "price": price,
                        "image_url": image_url
                    })
                    print(f"[DEBUG] Parsed product {i+1}: {title[:50]}... - ₹{price}")
                else:
                    print(f"[DEBUG] Failed to parse card {i+1}: title={bool(title)}, price={bool(price)}, image={bool(image_url)}")
                        
            except Exception as e:
                print(f"[WARN] Failed to parse card {i+1}: {e}")
                continue
                
        return items
    
    def extract_title(self, card):
        """Extract product title from card"""
        title_selectors = [
            "div[class*='KzDlHZ']",  # Main title selector
            "div[class*='_4rR01T']", # Old title selector
            "a[class*='IRpwTa']",    # Link title selector
            "div[class*='s1Q9rs']",  # Another title selector
            "div[class*='_2WkVRV']", # Yet another title selector
        ]
        
        for selector in title_selectors:
            element = card.select_one(selector)
            if element:
                title = element.get_text(strip=True)
                if title and len(title) > 5:  # Basic validation
                    return title
        
        return None
    
    def extract_price_from_card(self, card):
        """Extract price from card"""
        price_selectors = [
            "div[class*='Nx9bqj']",  # Main price selector
            "div[class*='_30jeq3']", # Old price selector
            "div[class*='_1_WHN1']", # Another price selector
            "div[class*='_25b18c']", # Yet another price selector
            "span[class*='_2-ut7f']", # Span price selector
        ]
        
        for selector in price_selectors:
            element = card.select_one(selector)
            if element:
                price_text = element.get_text(strip=True)
                price = self.extract_price(price_text)
                if price:
                    return price
        
        return None
    
    def extract_image_url(self, card):
        """Extract image URL from card"""
        image_selectors = [
            "img[class*='DByuf4']",  # Main image selector
            "img[class*='_396cs4']", # Old image selector
            "img[class*='_2r_T1I']", # Another image selector
            "img[class*='_3exPp9']", # Yet another image selector
        ]
        
        for selector in image_selectors:
            element = card.select_one(selector)
            if element:
                image_url = element.get('src') or element.get('data-src')
                if image_url and image_url.startswith('http'):
                    return image_url
        
        return None
    
    def extract_price(self, price_text):
        """Extract numeric price from text"""
        try:
            # Remove currency symbols and commas, extract numbers
            price_match = re.search(r'[\d,]+', price_text.replace('₹', '').replace(',', ''))
            if price_match:
                return float(price_match.group().replace(',', ''))
            return None
        except:
            return None

