# 🛒 Retail ETL Pipeline

This project showcases a scalable ETL pipeline using Python, SQL, and Power BI, built around a real-world retail dataset. It covers data extraction, transformation, loading, querying, and dashboarding.

---

## 📦 Dataset

- [Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Contains order, customer, shipping, and profit details.

---

## 🔧 Technologies Used

- **Python** – Core scripting for ETL
- **Pandas** – Data transformation
- **SQLite** – Local data storage
- **SQL** – Analysis and querying
- **Power BI** – Dashboarding
- **Modular Structure** – Separate scripts for each pipeline stage

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
python scripts/extract.py
python scripts/transform.py
python scripts/load.py

---

## 📁 Project Structure

retail-etl-pipeline/
├── data/                  # Raw input data
├── notebooks/             # Jupyter notebooks for EDA/SQL
├── output/                # Final outputs
│   ├── retail.db
│   ├── Retail_ETL_Dashboard.pbix
│   ├── charts/
│   └── exports/
├── sql/                   # SQL queries
├── scripts/               # Modular ETL scripts
├── requirements.txt
├── .gitignore
└── README.md


---

## 📊 Power BI Dashboard

Includes key visuals:

✅ Total Sales per Region

✅ Top Products by Sales

✅ Profit by Category

✅ Monthly Sales Trend

✅ Customer Frequency

✅ Filters for Region, Category

📸 ![Dashboard Preview](Retail_ETL_Dashboard Preview Map.png)



---

## 🧠 SQL Practice
Explore queries like:

```sql

-- Top 10 Selling Products
SELECT [Product Name], SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY [Product Name]
ORDER BY Total_Sales DESC
LIMIT 10;
Stored in:

```pgsql

sql/
├── top_10_products.sql
├── total_sales_by_region.sql
├── monthly_sales.sql
├── customer_frequency.sql
├── cumulative_sales_by_month.sql

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/retail-etl-pipeline.git
   cd retail-etl-pipeline

2. Set up your environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. Run the pipeline:

   ```bash
   python scripts/extract.py
   python scripts/transform.py
   python scripts/load.py


---

## 📦 Technologies
- Python (pandas, sqlite3)
- SQL (SQLite)
- Modular scripting (extract → transform → load)
- Designed for scalability to Azure SQL, Airflow, or dbt


---

## 🚀 Future Enhancements:

 - Migrate to Azure SQL

 - Automate ETL with Apache Airflow

 - Add unit tests and logging

 - Apply ML for forecasting & segmentation


---

🙋 Author
Venu Madhuri Yerramsetti
LinkedIn
📧 venumadhuri.y@gmail.com
---

## 💡 Author
[Venu Madhuri Yerramsetti]
[https://www.linkedin.com/in/venu-madhuri-yerramsetti-349057aa] | [Portfolio] | [venumadhuri.y@gmail.com]
