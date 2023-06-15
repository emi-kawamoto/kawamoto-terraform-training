from airflow import DAG
from airflow.operators.bash import BashOperator
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
    dag_id="sample_backfill",
    default_args=default_args,
    schedule_interval="0 0 * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False,  # 前回実行時点まで遡って実行しない
) as dag:
    print_ds = BashOperator(
        task_id="print_ds",
        bash_command="echo {{ ds }}",
    )

print_ds
