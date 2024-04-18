from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

from datetime import datetime, timedelta

def task(name,age):
    print(f"Hi, My name is {name} and age of {age}.")

default_args={"owner" : "mohan",
              "retries" : 2,
              "retry_delay" : timedelta(minutes=1)}


dag=DAG(dag_id="python_kwargs",
        description=" This is python key value arguments",
        default_args=default_args,
        start_date=datetime(2024,3,24,6),
        schedule_interval="@daily")

start = BashOperator(task_id="start",
                   bash_command="echo started the task",
                   dag=dag)

python_task = PythonOperator(task_id="python_task",
                             python_callable=task,
                             op_kwargs={'name':'mohan','age':23},
                             dag=dag)

end = BashOperator(task_id="end_task",
                   bash_command="echo ended the task",
                   dag=dag)

start>>python_task>>end
