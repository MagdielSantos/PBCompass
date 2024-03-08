import json
import requests
import boto3
from datetime import datetime
from config import AWS_ACESS_KEY, AWS_SECRET_KEY, AWS_SESSION_TOKEN

def main():
    tmdb_api_key = 'b2371456d16036107f5b9b1756aa4798'
    tmdb_endpoint = f'https://api.themoviedb.org/3/discover/movie?api_key={tmdb_api_key}&language=pt-BR'
    tmdb_params = {
        'api_key': tmdb_api_key,
        'with_genres': '18,10749', 
        'primary_release_date.gte': '2000-01-01',
        'primary_release_date.lte': '2020-12-31',
        'with_keywords': '818'
    }
    
    def create_s3_path(prefix, folder, extension, datetime, filename):
        return f"{prefix}/{folder}/{datetime.strftime('%Y/%m/%d')}/{filename}.{extension}"
    
    current_datetime = datetime.now()
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, aws_session_token=AWS_SESSION_TOKEN)
    bucket_name = 'datalake-magdiel'
    
    for page_group in range(1, 5):  # Fazendo 5 solicitações para obter 100 registros
        movie_data = []
        for page in range((page_group - 1) * 5 + 1, page_group * 5 + 1):
            tmdb_params['page'] = page
            response = requests.get(tmdb_endpoint, params=tmdb_params)
            response.raise_for_status()
            tmdb_data = response.json()
            movie_data.extend(tmdb_data['results'])
            
        
        file_name = f'tmdb_data_{current_datetime.strftime("%Y%m%d%H%M%S")}_group_{page_group}.json'
        file_path = create_s3_path('raw', 'tmdb', 'json', current_datetime, file_name)
        
        s3.put_object(Bucket=bucket_name, Key=file_path, Body=json.dumps(movie_data, indent=4, ensure_ascii=False))
    
if __name__ == '__main__':
    main()
