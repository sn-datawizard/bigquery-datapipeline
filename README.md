# BigQuery-Datapipeline

## Overview
Dataset source: NYC Yello Taxi Trip Records

## Prerequisites
### Dataset

To download the dataset execute the following command in your terminal:

```
wget <url> -O /path/to/filename.ext
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet -O /mnt/c/Users/Nikesh/Desktop/data.parquet
```

### Required python modules
```
pip3 install pyarrow
pip3 install fastparquet
pip3 install google-cloud-storage
pip3 install google-cloud-bigquery
pip3 install gcfsf
```

### GCP Project
1. Create new project
2. Create service account (Dashboard -> Project settings -> Service accounts)
3. Generate .json keyfile (click on created service account -> Open KEYS tab -> ADD KEY)
4. Move file in working directory
