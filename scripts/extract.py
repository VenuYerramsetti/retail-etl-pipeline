import pandas as pd

def extract_data(filepath="data/superstore.csv"):
    print("📦 Extracting data...")
    try:
        df = pd.read_csv(filepath, encoding="ISO-8859-1")
        print(f"✅ Data extracted: {df.shape[0]} rows, {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print(f"❌ File not found at: {filepath}")
        return None

if __name__ == "__main__":
    extract_data()
