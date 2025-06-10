# 🛒 Retail ETL Pipeline

This project showcases a simple but scalable ETL pipeline built in Python using a real-world retail dataset. It demonstrates key data engineering concepts such as ingestion, transformation, and loading into a local database.

---

## 📊 Dataset

- [Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Includes order details, shipping, customer info, sales, profit, etc.

---

## 🔧 Technologies Used

- **Python**: Data manipulation and scripting
- **Pandas**: Data processing
- **SQLite**: Local database storage
- **Modular ETL Structure**: `extract.py`, `transform.py`, `load.py`

---

## 🧱 Project Structure


retail-etl-pipeline/
├── data/ # Raw dataset
├── output/ # Transformed output CSVs
├── scripts/ # Modular ETL scripts
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── db/ # (optional) schema.sql
├── retail.db # Local SQLite DB
├── requirements.txt
├── .gitignore
└── README.md


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
- Cloud integration (Azure SQL / Azure Data Factory)
- Airflow DAG automation
- Power BI dashboards with DAX
- Machine Learning for sales forecasting & customer segmentation

---

## 📈 What’s Next

- Move SQLite DB to Azure SQL
- Automate ETL using Airflow
- Create Power BI dashboard
- Add machine learning models for forecasting or segmentation

---

## 💡 Author
[Venu Madhuri Yerramsetti]
[https://www.linkedin.com/in/venu-madhuri-yerramsetti-349057aa] | [Portfolio] | [venumadhuri.y@gmail.com]
