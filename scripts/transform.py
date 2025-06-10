# scripts/transform.py

import pandas as pd
from extract import extract_data

def transform_data(df):
    print("🔄 Transforming data...")
    
    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    
    # Calculate profit margin
    df["Profit Margin"] = df["Profit"] / df["Sales"]
    
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    print("✅ Data transformation complete.")
    return df

if __name__ == "__main__":
    df = extract_data("data/superstore.csv")
    transformed_df = transform_data(df)
    transformed_df.to_csv("output/transformed_superstore.csv", index=False)
    print("📁 Transformed data saved to output/transformed_superstore.csv")
