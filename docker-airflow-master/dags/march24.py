from airflow import DAG
from  airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime,timedelta




def task():
    print("this is python task got succeeded (^v^)")


default_args={"owner":"mohan",
             "start_date":datetime(2024,3,23),
             "schedule":"@daily"
                }



with DAG(dag_id='march_24_dag',default_args=default_args,tags='march') as dag:
    
    start_task=BashOperator(task_id='start',
                            bash_command='echo started the task',
                            retries=2)
    

    python_task=PythonOperator(task_id='python_task',
                               python_callable=task,
                               retries=2)
    
    email_task=EmailOperator(task_id='email_task',
                             to='kadulurimohansai884@gmail.com',
                             subject='This is email test TASK',
                             html_content="<h1> This is testing mail</h1>\
                                            <p> Hi,</p>\
                                            <p>This is mohan from infosys.</p>\
                                            <p>This is test mail for testing the aiflow code.</p>"
                             )
    
    end_task=BashOperator(task_id='end_task',
                          bash_command='echo ended the task')
    
    start_task>>python_task>>email_task>>end_task



    






