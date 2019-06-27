import boto3
import subprocess
import pandas as pd
import io

aws_id = 'AKIAZCV5L2QOTAU5WA4G'
aws_secret = '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'

s3 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
obj = s3.get_object(Bucket='excelbkt', Key='MOCK_SINGTEL_INGESTION_EXTRACT_2018-12-26.csv')
df = pd.read_csv(io.BytesIO(obj['Body'].read()))