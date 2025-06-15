#!/usr/bin/env python
# coding: utf-8

# run_pipeline.py — Master ETL pipeline script

import os
import pandas as pd
import sqlite3

# ✅ Use package imports
from scripts.extract import extract_data
from scripts.transform import transform_data

# File paths
RAW_CSV = "data/superstore.csv"
TRANSFORMED_CSV = "output/exports/transformed_superstore.csv"
SQLITE_DB = "output/retail_data.db"

def run_pipeline():
    print("🚀 Starting ETL pipeline...")

    # --- Extract ---
    df_raw = extract_data(RAW_CSV)
    if df_raw is None:
        print("❌ ETL pipeline stopped: raw data not found.")
        return

    # --- Transform ---
    df_transformed = transform_data(df_raw)

    # Save CSV
    os.makedirs("output/exports", exist_ok=True)
    df_transformed.to_csv(TRANSFORMED_CSV, index=False)
    print(f"📁 Transformed data saved to: {TRANSFORMED_CSV}")

    # --- Load ---
    conn = sqlite3.connect(SQLITE_DB)
    df_transformed.to_sql("superstore", conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Data loaded into database: {SQLITE_DB}")

    print("✅ ETL pipeline complete.")

if __name__ == "__main__":
    run_pipeline()
