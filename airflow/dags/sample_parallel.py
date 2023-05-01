from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from textwrap import dedent

# デフォルトの引数の定義、明示的に設定した値以外はこちらが参照される
default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "hoge@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="sample_parallel",
    default_args=default_args,
    schedule_interval="0 0 * * *",
    start_date=days_ago(0),  # 当日を設定
    catchup=False,  # 前回実行時点まで遡って実行しない
) as dag:
    t1 = BashOperator(
        task_id="print_start_date",
        bash_command="date",
    )
    t2 = BashOperator(
        task_id="sleep5s",
        depends_on_past=False,  # 以前のタスクが失敗しても実行する
        bash_command="sleep 5s",
    )
    t3 = BashOperator(
        task_id="sleep10s",
        depends_on_past=False,  # 以前のタスクが失敗しても実行する
        bash_command="sleep 10s",
    )
    # Jinja テンプレートでコマンドを作成（5回実行して実行日と実行日の7日後を標準出力）
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
    {% endfor %}
    """
    )
    t4 = BashOperator(
        task_id="templated",
        depends_on_past=False,  # 以前のタスクが失敗しても実行する
        bash_command=templated_command,
    )
    t5 = BashOperator(
        task_id="print_end_date",
        bash_command="date",
    )

t1 >> [t2, t3, t4] >> t5
