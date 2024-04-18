from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator 
from Kafka import consumer,producer
from datetime import datetime,timedelta



default_args={
    "owner" : "mohan",
    "start_date" : datetime(2024,4,2),
    "retries" : 2 ,
    "retry_delay" : timedelta(seconds=60)
}





with DAG(dag_id="first_kafka_dag",
         default_args=default_args,
         schedule_interval='@daily'


) as dag:

    start_task=BashOperator(task_id="start",
                            bash_command="echo started the task")
    
    producer_task = PythonOperator(task_id="Producer_task",
                                   python_callable=producer.main())
    
    consumer_task = PythonOperator(task_id="Consumer_task",
                                   python_callable=consumer.main())
    
    end_task = BashOperator(task_id="end",
                            bash_command="echo ended the task successfully")
    
    start_task>>producer_task>>consumer_task>>end_task



