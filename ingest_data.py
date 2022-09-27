import main

#Convert .parquet file to .csv file
main.convert_parquet_csv()

#Convert datetime to date
main.transform_data()

#Establish connection to Cloud Storage bucket
bucket = main.connection_cloudstorage()

#Upload .csv file to Cloud Storage
main.upload_cloudstorage(bucket)

#Upload .csv file stored in Cloud Storage to BigQuery
main.upload_bigquery()