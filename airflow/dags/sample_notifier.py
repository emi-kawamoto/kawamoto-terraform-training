from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

from notice.slack import post_error_slack


def failure_callback(context):
    URL = Variable.get("slack_url")
    post_error_slack(URL, context)


# デフォルトの引数の定義、明示的に設定した値以外はこちらが参照される
default_args = {
    "owner": "airflow",
    "email_on_failure": False,  #
    "email_on_retry": False,
    "email": "hoge@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "on_failure_callback": failure_callback,  # すべてのタスクについて失敗時に通知する
}

with DAG(
    dag_id="sample_notifier",
    default_args=default_args,
    schedule_interval="0 0 * * *",
    start_date=days_ago(0),  # 当日を設定
    catchup=False,  # 前回実行時点まで遡って実行しない
) as dag:
    # わざとエラーにする
    test_error = BashOperator(task_id="test_error", bash_command="exit 1")

test_error
