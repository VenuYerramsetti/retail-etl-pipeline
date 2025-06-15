import pandas as pd
from scripts.extract import extract_data  # ✅ Fixed import

def transform_data(df):
    print("🔄 Transforming data...")

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Add profit margin
    df["Profit Margin"] = df["Profit"] / df["Sales"]

    # Drop missing rows
    df.dropna(inplace=True)

    print("✅ Data transformation complete.")
    return df

# Optional test
if __name__ == "__main__":
    df = extract_data("data/superstore.csv")
    transformed_df = transform_data(df)
    transformed_df.to_csv("output/exports/transformed_superstore.csv", index=False)
    print("📁 Transformed data saved to: output/exports/transformed_superstore.csv")
