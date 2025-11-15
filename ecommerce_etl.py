from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import boto3
from botocore.client import Config
import os

# MinIO connection config
MINIO_ENDPOINT = "***"
MINIO_ACCESS_KEY = "****"
MINIO_SECRET_KEY = "*****"
MINIO_BUCKET = "ecommerce-bucket"
S3_KEY = "processed/ecommerce_cleaned.csv"

RAW_FILE = "/opt/airflow/data/ecommerce_raw.csv"
PROCESSED_FILE = "/opt/airflow/output/ecommerce_cleaned.csv"

def extract():
    df = pd.read_csv(RAW_FILE, encoding_errors='replace')
    print(f"Extracted {len(df)} rows from {RAW_FILE}")
    return df.to_dict(orient='records')

def transform(**context):
    records = context['ti'].xcom_pull(task_ids='extract')
    df = pd.DataFrame(records)
    df = df[df['Country'] == 'France']
    summary = df.groupby('InvoiceNo')['UnitPrice'].sum().reset_index()
    summary.to_csv(PROCESSED_FILE, index=False)
    print(f"Transformed data saved to {PROCESSED_FILE}")
    return PROCESSED_FILE

def load(**context):
    s3 = boto3.client(
        's3',
        endpoint_url=f"http://{MINIO_ENDPOINT}",
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
        config=Config(signature_version='s3v4'),
        region_name='us-east-1'
    )

    # Ensure bucket exists
    buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]
    if MINIO_BUCKET not in buckets:
        s3.create_bucket(Bucket=MINIO_BUCKET)

    s3.upload_file(PROCESSED_FILE, MINIO_BUCKET, S3_KEY)
    print(f"File uploaded to MinIO: {MINIO_BUCKET}/{S3_KEY}")

default_args = {
    'owner': 'kindoli',
    'start_date': datetime(2025, 11, 12),
    'retries': 1,
}

with DAG(
    'ecommerce_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    t1 = PythonOperator(task_id='extract', python_callable=extract)
    t2 = PythonOperator(task_id='transform', python_callable=transform)
    t3 = PythonOperator(task_id='load', python_callable=load)

    t1 >> t2 >> t3
