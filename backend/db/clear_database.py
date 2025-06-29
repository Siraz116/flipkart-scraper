# backend/db/clear_database.py

import sys
import os

# Add parent directory to path to import config and database
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_CONFIG
from db.database import MySQLDatabase

def clear_database():
    """Clear all data from the product_info table"""
    
    try:
        # Connect to database
        print("[INFO] Connecting to database...")
        db = MySQLDatabase(DB_CONFIG)
        
        # Get current count
        db.cursor.execute("SELECT COUNT(*) FROM product_info")
        current_count = db.cursor.fetchone()[0]
        print(f"[INFO] Current products in database: {current_count}")
        
        if current_count == 0:
            print("[INFO] Database is already empty!")
            return
        
        # Confirm deletion
        response = input(f"\n[CONFIRM] Delete all {current_count} products? (y/N): ")
        if response.lower() != 'y':
            print("[INFO] Deletion cancelled.")
            return
        
        # Delete all data
        print("[INFO] Deleting all products...")
        db.cursor.execute("DELETE FROM product_info")
        db.conn.commit()
        
        # Verify deletion
        db.cursor.execute("SELECT COUNT(*) FROM product_info")
        new_count = db.cursor.fetchone()[0]
        
        print(f"[SUCCESS] Deleted {current_count} products!")
        print(f"[INFO] Products remaining: {new_count}")
        
        db.close()
        
    except Exception as e:
        print(f"[ERROR] Failed to clear database: {e}")
        print("[ERROR] Please check:")
        print("   1. MySQL server is running")
        print("   2. Database credentials are correct")
        print("   3. Database and table exist")

if __name__ == "__main__":
    clear_database() 