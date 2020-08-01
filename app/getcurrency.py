import csv
import logging
import os
import requests
import urllib3
import datetime as dt
'''from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.models import Variable
from google.cloud import storage
from airflow.contrib.operators import dataproc_operator'''

logging.getLogger("urllib3").setLevel(logging.WARNING)


# Defining a DAG to schedule the same every one hour
# with DAG(dag_id = "curency_api_dag") as dag: 
'''PIPELINE_ID = 1

start_date = datetime(2020, 7, 31);

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': start_date,
    'email': ['sidgk248@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = airflow.DAG(
    dag_id='currency_api_fetch_dag',
    schedule_interval="0 23 * * *",
    default_args=default_args)
'''
# Class to read and load the currency data into CSV file
class CurrencyDownloader():
    def __init__(self,url):
        self.url = url

    # Check the correctness of the URL
    def checkURL(self):
        if self.url is not None:
            response = requests.get(self.url)
            logging.info("URL {} to download data from.".format(self.url))
            logging.info("Checking status of given URL ...")
            if response.status_code == 200:
                logging.info("Success! {}".format( response.status_code))
            elif response.status_code == 404:
                logging.info("Not Found! {}".format(response.status_code))
            else:
                logging.info("Something went wrong URL {} with status ".format(self.url,response.status_code))
    
    # Download the data to CSV file
    def downloadData(self):
        response = None
        fpath = './data/downloads/sample.csv'
        logging.info("Data will be downloaded into {}".format(fpath))
        file_exists = os.path.isfile(fpath)

        # Exception handling to gracefuly end the program incase any error occur with the appropriate error message 
        try:
            response = requests.get(self.url).json()
        except requests.exceptions.ConnectionError as err:
            logging.error('Connection failed- {}'.format(str(err)))
        except urllib3.exceptions.MaxRetryError as err:
            logging.error('Connection failed, Maximum retry occured {}'.format(str(err)))

        if response is not None:
            try:
                with open(fpath, 'a') as out:
                    data = response

                    fieldnames = ['Base', 'Date', 'CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON', 'SEK',
                                  'IDR',
                                  'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR', 'BGN', 'TRY', 'CNY',
                                  'NOK', 'NZD',
                                  'ZAR', 'USD', 'MXN', 'SGD', 'AUD', 'ILS', 'KRW', 'PLN']
                    logging.info("Columns- {}".format(fieldnames))
                    writer = csv.DictWriter(out, fieldnames=fieldnames)

                    if not file_exists:
                        writer.writeheader()
                    logging.info("{} file exists {}".format(fpath,file_exists))
                    row = data['rates']
                    row.update(Base=data['base'], Date=data['date'])
                    logging.info("Latest currency {} to be inserted into file {}".format(row,fpath))
                    writer.writerow(row)
                    logging.info("Currency fetch success.")
            except FileNotFoundError as err:
                logging.error('Trying to download file {}'.format(str(err)))
            except Exception as err:
                logging.error('Downloading file failed due to {}'.format(str(err)))

    def checkAndDownloadData(self):
        self.checkURL()
        self.downloadData()

# 

#checkAndDownloadData()

'''convert_currency =  PythonOperator(
    task_id='load_currency_to_CSV',
    python_callable=checkAndDownloadData,
    dag=dag)
#Created dummy task to explain Dependencies section.
t_first_task = DummyOperator(
    task_id='first_task',
    dag=dag
)'''
# Dependencies, Tell airflow the order of execution
# set_upstream() : task execution happens from right to left
# set_downstream() : task execution happens from left to right, as described below. Meaning first t_first_task will execute and followed by convert_currency task
 
#t_first_task.set_downstream(convert_currency)
