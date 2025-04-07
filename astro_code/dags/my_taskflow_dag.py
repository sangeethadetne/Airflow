from airflow import DAG
from datetime import datetime
from airflow.decorators import dag, task

@dag('taskflow_API_dag',
     start_date = (2025,1,1),
     schedule = '@daily',
     tags =['taskflow_API_dag'],
     catchup =False,
     description = 'This dag is created by the taskflow API'
     )
def taskflow_API_dag():
    
    @task
    def print_a():
        print("Hi from task_a")