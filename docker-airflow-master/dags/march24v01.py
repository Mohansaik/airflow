from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime,timedelta


def task():
    print(" this is complex python task")


default_args={'owner':'mohan',
              'start_date':datetime(2024,3,24),
              'schedule': timedelta(hours=9,minutes=20)}

dag=DAG(dag_id='complex_dag',default_args=default_args)



beginning_task=BashOperator(task_id="Beginning_task",bash_command='echo started the complex dag',dag=dag)


email_task=EmailOperator(task_id="Email_task",
                         to=['kadulurimohansai884@gmail.com','komali.kaduluri0125@gmail.com'],
                         subject='This mail was regarding Complex task',
                         html_content="<h1> Complex DAG Result </h1>\
                                        <p>Hi Team,</p>\
                                        <p>I'm Mohan working on infosys. This mail was regarding complex dag execution which got executed successfully</p>\
                                        <p>Thanks & Regards,</p>\
                                        <p>Mohan Sai Kaduluri</p> ",
                        dag=dag
                         )

for i in range(1,6):
    start_task=BashOperator(task_id=f"start_task_{i}",bash_command=f"echo this is {i} th start task",dag=dag)

    python_task=PythonOperator(task_id=f"python_task_{i}",python_callable=task,dag=dag)

    end_task=BashOperator(task_id=f"end_task_{i}",bash_command=f"echo this is {i}th end task",dag=dag)


    beginning_task>>start_task>>python_task>>end_task>>email_task

