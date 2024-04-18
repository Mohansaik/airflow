from airflow import DAG
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime,timedelta

def task1(name,age):
    print(f"Hi I'm {name} of {age}.")



default_args={
    "owner" : "mohan",
    "retries" : 2,
    "retry_delay" : timedelta(minutes=1)
}


dag=DAG(
    dag_id="python_args",
    default_args=default_args,
    start_date=datetime(2024,3,24,9),
    schedule_interval ='@daily'
    )

start_task = BashOperator(task_id="start",
                          bash_command='echo started the task',
                          dag=dag)


python_task = PythonOperator(task_id="python_task",
                            python_callable=task1,
                            op_args=['mohan',23],
                            dag=dag)

end_task = BashOperator(task_id="end",
                        bash_command='echo ended the task',
                        dag=dag)

email_task = EmailOperator(task_id="email_task",
                           to= 'kadulurimohansai884@gmail.com',
                           subject='pyhton args testing',
                           html_content= "<h1> Congratulations! </h1> \
                             <p> Python arguments testing was successfulll </p> ",
                             dag=dag)

start_task>>python_task>>email_task>>end_task