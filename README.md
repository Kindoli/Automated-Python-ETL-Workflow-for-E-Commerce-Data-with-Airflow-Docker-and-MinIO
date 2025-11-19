## E-Commerce ETL Pipeline with Airflow, Python & MinIO


<p align="center">
<img width="202" height="101" alt="Banner" src="https://github.com/user-attachments/assets/5cb99204-6f3c-4c28-a684-0ed8f21d9148" />
</p>


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

Filters only transactions from France and Germany

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
  
- PowerBI

  ## PowerBI Dashboard

  <img width="602" height="377" alt="Dashboard" src="https://github.com/user-attachments/assets/3f350c7e-37d2-4cea-aa61-40ce5a51ee55" />

  
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
