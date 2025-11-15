## E-Commerce ETL Pipeline with Airflow, Python & MinIO

This project demonstrates a beginner-friendly batch ETL pipeline built with Apache Airflow, Python, Docker, and MinIO (as an S3-compatible object store).
The workflow extracts raw e-commerce transactions, performs cleaning and transformation with Pandas, and loads processed output into MinIO for analytics and reporting.

## Project Architecture

The pipeline includes:

Airflow Scheduler & Webserver – for workflow orchestration

MinIO – S3-like storage for processed files

Airflow DAG – Python-based ETL steps

Docker Compose – fully containerized setup

Volumes – persistent storage for raw and processed data

## 📁 ETL Workflow
🔹 Extract

Reads the raw CSV file (ecommerce_raw.csv) from /opt/airflow/data/.

🔹 Transform

Applies cleaning and filtering using Pandas:

Filters only transactions from France

Aggregates unit prices by InvoiceNo

Saves output to /opt/airflow/output/ecommerce_cleaned.csv

🔹 Load

Uploads the cleaned CSV file to MinIO bucket:

ecommerce-bucket/processed/ecommerce_cleaned.csv

## Architecture Diagram

![Ecommerce2](https://github.com/user-attachments/assets/f59bf364-6de2-4ac3-b5bd-3c45f0dfa861)


##  Project Structure
├── dags/

│   └── ecommerce_etl.py

├── data/

│   └── ecommerce_raw.csv
├── output/

├── docker-compose.yml

└── README.md

## 🧪 Technologies Used

- Python (Pandas, Boto3)
  
- Apache Airflow

- MinIO (S3 API)

- Docker & Docker Compose
  
  ## 🛡️ Best Practices Implemented

✔ Environment variables for secrets (secret key, MinIO creds)

✔ No hard-coded passwords in code

✔ XCom used only for lightweight metadata

✔ Large data passed via files instead of XCom

✔ Modular project structure (dags / data / output)

✔ Proper volume mounting for reproducibility

✔ Idempotent DAG tasks (overwrite allowed)

## 🎯 Key Learning Outcomes

- How to design a batch ETL pipeline using Airflow

- Working with XComs and PythonOperators

- Integrating Airflow with S3-compatible storage

- Using Docker Compose to simulate a production-like environment
