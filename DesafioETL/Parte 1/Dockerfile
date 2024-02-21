FROM python:3.9

WORKDIR /app

COPY Upar.py configs.py /app/

COPY CSV/ /app/CSV/

RUN pip install boto3

CMD ["python", "/app/Upar.py"]
