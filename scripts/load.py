# scripts/load.py

import pandas as pd
import sqlite3
import os

def load_to_sqlite(csv_path, db_path="output/retail_data.db"):
    print("⬆️ Loading data into SQLite...")
    
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Connect to SQLite DB (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_path)
    
    # Load DataFrame to table 'superstore'
    df.to_sql("superstore", conn, if_exists="replace", index=False)
    
    conn.close()
    print(f"✅ Data loaded to SQLite database at: {db_path}")

if __name__ == "__main__":
    load_to_sqlite("output/transformed_superstore.csv")
