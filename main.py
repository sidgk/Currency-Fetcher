import sys
from os.path import dirname
sys.path.append(dirname(__file__))
import logging
from configparser import ConfigParser
from app.getcurrency1 import CurrencyDownloader
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta


config = ConfigParser()
# config.read('./config/config.ini')
url = "https://api.exchangeratesapi.io/latest?base=USD"
PIPELINE_ID = 1

start_date = datetime(2020, 7, 12)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': start_date,
   # 'email': ['sidgk248@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='currency_api_fetch_dag',
    schedule_interval="0 * * * *",
    default_args=default_args,
    catchup=True)


def downloadfile():
    reviewsDownloader = CurrencyDownloader(url)
    reviewsDownloader.checkAndDownloadData()

def main():
    logging.basicConfig(format='%(levelname)s %(asctime)s :: %(message)s',filename='./logs/myapp.log', level=logging.INFO)
    logging.info('Starting application...')
    downloadfile()
    logging.info('Application Finished.')

convert_currency =  PythonOperator(
    task_id='load_currency_to_CSV',
    python_callable=downloadfile,
    dag=dag)
#Created dummy task to explain Dependencies section.
t_first_task = DummyOperator(
    task_id='first_task',
    dag=dag
)
t_first_task >> convert_currency
#if __name__ == "__main__":
#    main()
