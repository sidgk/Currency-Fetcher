# Working with API's
Write a Python application that fetches
conversion rates for USD hourly, and appends them to a CSV file for further analysis. The structure of
the dataset should ease the purpose of our data scientist and will be decided by you. You can use
the API at https://exchangeratesapi.io/ 
## Prerequisites

```
pip install requests
pip install responses
pip install urllib3
pip install configparser
pip install mysql-connector-python
pip install unittest

OR 

pip install -r requirements.txt --> Because i have added all the required packages in requirements.txt.

```
# Summary
1. Initialy we are downloading the data from the given URL and saving it to sample_us.tsv file.
2. Creating the database connection and creating the database table to load the data in tsv file. 
3. Querying the data in the table and storing the query results to sample_results.csv under queries folder.
4. All the above code is written with Exceptions handling by recording everyactions with respective message to myapp.log file created under logs folder. 

# How to run the application 
There are 5 files in the main folder
1. **getdata.py** --> This file contains the code with exception handeling and with the logs to check if the URL provided to download the data is correct or not, if it is correct than write and store the data in a folder.
2. **dbload.py**  --> This file contains the code with exception handeling and with the logs to load the downloaded data into MySQL database that is installed in my local machine. Shows how the table was created and data was loaded into the tablename "sample"
3. **queries.py** --> This file contains the code with exception handeling and with the logs of the SQL queries you want to perform on the data in the sample table and the query results are stored in the sample_result.csv
4. **main.py** --> This file contains all the functionalities developed in above 3 files and runs the application with all the necessary exceptins and logs, and stores them in the logger file **myapp.log**
5. **config.ini** --> This file contains all the confidential details about the application, and it can be accessed by referencing to this file by using _ConfigParser_ module.

**I have used MySql as the database as i had it installed locally. It can be replaced with inmemory database like SqLite also.**


