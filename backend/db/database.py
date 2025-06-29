# backend/db/database.py

import mysql.connector

class MySQLDatabase:
    def __init__(self, config):
        try:
            self.conn = mysql.connector.connect(**config)
            self.cursor = self.conn.cursor()
            print("[DB] Connected to MySQL successfully.")
        except mysql.connector.Error as err:
            print(f"[ERROR] Database connection failed: {err}")
            raise

    def create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS product_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            image_url TEXT,
            price FLOAT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.cursor.execute(create_table_sql)
        self.conn.commit()
        print("[DB] Table 'product_info' ensured.")

    def insert_product(self, title, image_url, price):
        try:
            insert_sql = """
            INSERT INTO product_info (title, image_url, price)
            VALUES (%s, %s, %s)
            """
            self.cursor.execute(insert_sql, (title, image_url, price))
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"[ERROR] Failed to insert product: {err}")

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("[DB] Connection closed.")
