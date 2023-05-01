from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# 引数を受け取る形に修正
def _print(x):
    print(x)


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
    dag_id="sample_hello_refactoring",
    default_args=default_args,
    schedule_interval="0 0 * * *",
    start_date=days_ago(0),  # 当日を設定
    catchup=False,  # 前回実行時点まで遡って実行しない
) as dag:
    hello = PythonOperator(
        task_id="hello",
        python_callable=_print,
        op_kwargs={"x": "Hello!"},  # 引数の設定
    )
    goodbye = PythonOperator(
        task_id="goodbye",
        python_callable=_print,
        op_kwargs={"x": "Goog Bye!"},  # 引数の設定
    )

hello >> goodbye
