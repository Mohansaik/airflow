from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator 


default_args={"owner":"airflow","start_date":datetime(2024,3,20)}


def process():
    print("process has started")

with DAG(dag_id='first_dag',default_args=default_args,schedule_interval="@daily") as dag:
    
    check_file=BashOperator(task_id='check_file',
                            bash_command="shasum ~/ip_files/or.csv",
                            retries=2,
                            retry_delay=timedelta(seconds=15))
    
    process_task=PythonOperator(task_id='process_task',python_callable=process)
    
    check_file>>process_task

