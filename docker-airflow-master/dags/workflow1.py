from  airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime,timedelta




default_args={"owner":'airflow',"start_date":datetime(2024,3,20)
              
              
              }

with DAG(dag_id='Workflow_spark',default_args=default_args) as dag:

    start_task=BashOperator(task_id='start',
                            bash_command="echo Started spark task")
    # spark_task=PythonOperator(task_id='sample_spark_task',
    #                           python_callable=sample,
    #                           retries=2)
    task_spark_job = SparkSubmitOperator(
    task_id='spark_task',
    conn_id='spark_default',  # Connection ID to your Spark cluster
    application='~/dags/spark1.py')

    end_task=BashOperator(task_id='end',
                          bash_command=" echo ended the spark task")
    
    start_task>>task_spark_job>>end_task

