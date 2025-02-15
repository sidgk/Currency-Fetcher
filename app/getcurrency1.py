import sys
from os.path import dirname
sys.path.append(dirname(__file__))
import csv
import logging
import os
import requests
import urllib3
import datetime as dt

FILE_SAVE_PATH = "/home/ec2-user/airflow/results.csv"

logging.getLogger("urllib3").setLevel(logging.WARNING)

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
        logging.info("Data will be downloaded into {}".format(FILE_SAVE_PATH))
        file_exists = os.path.isfile(FILE_SAVE_PATH)
        if file_exists:
            logging.info("File is present in the path")
        else:
            logging.info("File dose not exist in path")
        # Exception handling to gracefuly end the program incase any error occur with the appropriate error message 
        file_exists_to = os.path.isfile(FILE_SAVE_PATH)
        if file_exists_to:
            logging.info("File is present in the path")
        else:
            logging.info("File dose not exist in path")
        try:
            response = requests.get(self.url).json()
        except requests.exceptions.ConnectionError as err:
            logging.error('Connection failed- {}'.format(str(err)))
        except urllib3.exceptions.MaxRetryError as err:
            logging.error('Connection failed, Maximum retry occured {}'.format(str(err)))

        if response is not None:
            try:
                with open(FILE_SAVE_PATH, 'a') as out:
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
                    logging.info("{} file exists {}".format(FILE_SAVE_PATH,file_exists))
                    row = data['rates']
                    row.update(Base=data['base'], Date=data['date'])
                    logging.info("Latest currency {} to be inserted into file {}".format(row,FILE_SAVE_PATH))
                    writer.writerow(row)
                    logging.info("Currency fetch success.")
           # except FileNotFoundError as err:
               # logging.error('Trying to download file {}'.format(str(err)))
            except Exception as err:
                logging.error('Downloading file failed due to {}'.format(str(err)))

    def checkAndDownloadData(self):
        self.checkURL()
        self.downloadData()

#checkAndDownloadData()

