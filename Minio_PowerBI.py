from minio import Minio
import pandas as pd
from io import BytesIO

# Connect to MinIO
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

# Download CSV from 'processed' folder
obj = client.get_object("ecommerce-bucket", "processed/ecommerce_cleaned.csv")
data = BytesIO(obj.read())

# Load CSV into DataFrame
df = pd.read_csv(data)

df
