# dags/example_dag.py
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    'example_bigquery_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    bigquery_task = BigQueryExecuteQueryOperator(
        task_id='read_bigquery_table',
        sql='SELECT * FROM `your_project.your_dataset.your_table` LIMIT 10',
        use_legacy_sql=False,
    )

    bigquery_task
