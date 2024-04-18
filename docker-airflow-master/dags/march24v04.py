from airflow import DAG
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import PythonOperator 
from datetime import datetime, timedelta

def name():
    return 'mohan'

def age():
    return 23

def sample(ti, **kwargs):
    name_value = ti.xcom_pull(task_ids='name')
    age_value = ti.xcom_pull(task_ids='age')
    print(f"My name is {name_value} and my age is {age_value}.")


default_args = {
    "owner": "mohan",
    "retries": 2,
    "retry_delay": timedelta(minutes=1) 
}

dag = DAG(
    dag_id='xcoms_dag',
    default_args=default_args,
    start_date=datetime(2024, 3, 23),
    schedule_interval='@daily',
)

task1 = BashOperator(
    task_id="start",
    bash_command="echo started the task",
    dag=dag
)

name_task = PythonOperator(
    task_id="name",
    python_callable=name,
    dag=dag
)

age_task = PythonOperator(
    task_id='age',
    python_callable=age,
    dag=dag
)

py_task = PythonOperator(
    task_id='py_task',
    python_callable=sample,
    provide_context=True,  # This allows passing task instance context to the function
    dag=dag
)

task2 = BashOperator(
    task_id="end",
    bash_command="echo ended the task",
    dag=dag
)

task1 >> [name_task, age_task] >> py_task >> task2
