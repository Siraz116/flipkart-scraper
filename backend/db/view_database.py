# backend/db/view_database.py

import sys
import os

# Add parent directory to path to import config and database
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_CONFIG
from db.database import MySQLDatabase

def view_database():
    """View all products in the database"""
    
    try:
        # Connect to database
        print("[INFO] Connecting to database...")
        db = MySQLDatabase(DB_CONFIG)
        
        # Get all products
        print("[INFO] Fetching all products...")
        db.cursor.execute("SELECT * FROM product_info ORDER BY created_at DESC")
        products = db.cursor.fetchall()
        
        print(f"\n[INFO] Found {len(products)} products in database:")
        print("=" * 80)
        
        if products:
            for i, product in enumerate(products, 1):
                print(f"\n{i}. ID: {product[0]}")
                print(f"   Title: {product[1][:100]}...")
                print(f"   Price: ₹{product[3]}")
                print(f"   Image: {product[2][:50]}...")
                print(f"   Created: {product[4]}")
                print("-" * 40)
        else:
            print("[INFO] No products found in database.")
            print("[INFO] This means either:")
            print("   1. The scraper hasn't run yet")
            print("   2. The scraper ran but found no products")
            print("   3. There was an error during scraping")
        
        # Show table structure
        print(f"\n[INFO] Table structure:")
        db.cursor.execute("DESCRIBE product_info")
        columns = db.cursor.fetchall()
        for column in columns:
            print(f"   {column[0]} - {column[1]}")
        
        db.close()
        
    except Exception as e:
        print(f"[ERROR] Failed to view database: {e}")
        print("[ERROR] Please check:")
        print("   1. MySQL server is running")
        print("   2. Database credentials are correct")
        print("   3. Database and table exist")

if __name__ == "__main__":
    view_database() 