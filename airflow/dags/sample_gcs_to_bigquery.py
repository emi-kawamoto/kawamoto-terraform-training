from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.contrib.operators import gcs_to_bq
from datetime import datetime, timedelta

# デフォルトの引数の定義、明示的に設定した値以外はこちらが参照される
default_args = {
    "owner": "airflow",
    "email_on_failure": False,  #
    "email_on_retry": False,
    "email": "hoge@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="sample_gcs_to_bigquery",
    default_args=default_args,
    schedule_interval="0 0 * * *",
    start_date=days_ago(0),
    catchup=False,  # 前回実行時点まで遡って実行しない
) as dag:

    # task1
    gcs_to_bq = gcs_to_bq.GoogleCloudStorageToBigQueryOperator(
        task_id="gcs_to_bq",
        bucket="base-airflow",
        source_objects=["weather_202201.csv"],
        skip_leading_rows="1",
        destination_project_dataset_table="<BigQueryの自分のデータセット名>.weather",
        schema_fields=[
            {"name": "id", "type": "STRING", "mode": "REQUIRED"},
            {"name": "date", "type": "DATETIME", "mode": "REQUIRED"},
            {"name": "tmin", "type": "NUMERIC", "mode": "NULLABLE"},  # 最低気温
            {"name": "tmax", "type": "NUMERIC", "mode": "NULLABLE"},  # 最高気温
            {"name": "prcp", "type": "NUMERIC", "mode": "NULLABLE"},  # 降水量
        ],
        write_disposition="WRITE_TRUNCATE",
        create_disposition="CREATE_IF_NEEDED",
    )

gcs_to_bq
