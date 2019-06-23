import boto3
import subprocess
import pandas as pd
import io

s3 = boto3.client('s3')
obj = s3.get_object(Bucket='excelbkt', Key='MOCK_SINGTEL_INGESTION_EXTRACT_2018-12-26.csv')
df = pd.read_csv(io.BytesIO(obj['Body'].read()))