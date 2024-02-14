import boto3
REGION = 'us-east-1'
ACCESS_KEY_ID = 'AKIAQN7UDSACDBS7HCUD'
SECRET_ACCESS_KEY = '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'
 
PATH_IN_COMPUTER = 'Desafio/Parte1/arquivo.txt'
 
BUCKET_NAME = 'teste-magdiel'
KEY = 'teste-magdiel/arquivo.txt' # file path in S3
 
s3_resource = boto3.resource(
    's3',
    region_name = REGION,
    aws_access_key_id = ACCESS_KEY_ID,
    aws_secret_access_key = SECRET_ACCESS_KEY
)

s3_resource.Bucket(BUCKET_NAME).put_object(
    Key = KEY,
    Body = open(PATH_IN_COMPUTER, 'rb')
)