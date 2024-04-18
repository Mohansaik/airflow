from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import BranchPythonOperator,PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta


def taskA():
    return 'condition_met'

default_args = {
    "owner": "mohan",
    "retries": 2,
    "retry_delay": timedelta(minutes=1) 
}

# Define branching condition function
def decide_branch(ti,**kwargs):
    # print(kwargs['task_instance'].xcom_pull(task_ids='task_A'))
    # task_instance = kwargs['task_instance']
    result = ti.xcom_pull(task_ids='task_A')
    if result == 'condition_met':
        return 'branch_A'
    else:
        return 'branch_B'

# Define DAG
dag = DAG(
    'branching_example',
    default_args=default_args,
    description='Example DAG with branching',
    schedule_interval=None,  # Set to None to trigger manually or via external trigger
    start_date=days_ago(1),
)

# Define tasks
task_A = PythonOperator(task_id='task_A',
                        python_callable=taskA ,
                        dag=dag)
branching_condition = BranchPythonOperator(task_id='branching_condition', python_callable=decide_branch, provide_context=True, dag=dag)
branch_A = DummyOperator(task_id='branch_A', dag=dag)
branch_B = DummyOperator(task_id='branch_B', dag=dag)
end = BashOperator(task_id='end',bash_command="echo ended the task ", dag=dag)

# Define task dependencies
task_A >> branching_condition >> [branch_A, branch_B] >> end