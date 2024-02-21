import boto3
import os
import datetime  
from configs import AWS_SESSION_TOKEN, AWS_ACCESS_KEY_ID, AWS_REGION,AWS_SECRET_ACCESS_KEY

# Configurações
BUCKET_NAME = 'datalake-magdiel'
LOCAL_CSV_FOLDER = '/app/CSV'


# iniciar sessão
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION
)

for csv_file in os.listdir(LOCAL_CSV_FOLDER):
 
    local_csv_path = os.path.join(LOCAL_CSV_FOLDER, csv_file)

    s3_key = f"Raw/Local/CSV/{os.path.splitext(csv_file)[0]}/{datetime.datetime.now().strftime('%Y')}/{datetime.datetime.now().strftime('%m')}/{datetime.datetime.now().strftime('%d')}/{os.path.basename(local_csv_path)}"

    s3_client.upload_file(local_csv_path, BUCKET_NAME, s3_key)

    print(f"Arquivo {local_csv_path} enviado para {s3_key} no S3.")
