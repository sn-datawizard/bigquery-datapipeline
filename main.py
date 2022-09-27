import pandas as pd
from google.cloud import storage
from google.cloud import bigquery

keyfile = './bigquery-project-363810-27f0aaf8ab88.json'

def convert_parquet_csv():
    df = pd.read_parquet('data.parquet')
    df.to_csv('data.csv', sep=';', decimal=',', index=False)
    print('parquet to csv DONE')

def transform_data():
    df = pd.read_csv("data.csv", sep=';', nrows=100, index_col=False)
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['tpep_pickup_datetime'] = df['tpep_pickup_datetime'].dt.date
    df['tpep_dropoff_datetime'] = df['tpep_dropoff_datetime'].dt.date
    df.to_csv('data.csv', sep=';', decimal=',', index=False)
    print('datetime to date transformation DONE')

def connection_cloudstorage():
    client = storage.Client.from_service_account_json(keyfile)
    buckets_list = list(client.list_buckets())
    print(buckets_list)
    bucket = client.get_bucket('taxi-data-bucket1')
    return bucket

def upload_cloudstorage(bucket):    
    blob = bucket.blob('data') #Target path
    blob.upload_from_filename('./data.csv') #Source path

    print(blob.public_url)
    print('Upload successfull')

def upload_bigquery():
    client = bigquery.Client.from_service_account_json(keyfile)

    df = pd.read_csv('gs://taxi-data-bucket1/data', sep=';', nrows=100, index_col=False, storage_options={'token': keyfile})
    df = df.drop(df.columns[0], axis=1)

    table_id = "bigquery-project-363810.taxi_dataset.table1"

    job = client.load_table_from_dataframe(df, table_id)
    print('Upload done')