import sqlite3
import pandas as pd

csv_path = "output/exports/transformed_superstore.csv"
db_path = "output/retail_data.db"

print("⬆️ Loading data into SQLite...")

df = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)
df.to_sql("superstore", conn, if_exists="replace", index=False)
conn.close()

print(f"✅ Data loaded into DB: {db_path}")
