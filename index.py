import datetime as dt 
from datetime import date
from dateutil.relativedelta import relativedelta

import xlrd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import xlrd

import plotly
plotly.tools.set_credentials_file(username='SandeepSingh', api_key='UnB6UI5RTJVMzzK4eQUx')
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import IFrame

from string import Template

#pulling the excel file into a variable, excelname

excelname = 'E:\\PythonProjects\\pyData\DataDump\\CSV_SINGTEL_INGESTION_EXTRACT_2018-12-26.csv'

#creating the dataframe, df

df = pd.read_csv(excelname)

#setting a variable for 3 months

three_months = date.today() + relativedelta(months=+3)
mth3 = pd.to_datetime(three_months)

#creating a variable called todaydate to capture today's date

todaydate = pd.datetime.now()

#creating pre-set lists

country = ['indonesia', 'thailand', 'philiphines', 'singapore', 'india']
countrycode = ['ID', 'TH', 'PH', 'SG', 'IN']
sublanguage = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu']
audiolanguage = ['english', 'bahasa', 'thai', 'mandarin', 'hindi', 'tamil', 'telegu']

#empty lists

subtitlelist = []
audiolist = []



for a, b in zip(sublanguage, audiolanguage):
    text = "subtitle_"
    text2 = "audiolanguage_"
    subtitlelist.append(text + a)
    audiolist.append(text2 + b)

subtitleaudiolist = subtitlelist + audiolist

for i in subtitleaudiolist:
    df[i] = df[i].str.strip()

licensedates = ['lic_start_date_indonesia', 'lic_end_date_indonesia', 'lic_start_date_thailand', 'lic_end_date_thailand',
               'lic_start_date_philiphines', 'lic_end_date_philiphines', 'lic_start_date_singapore', 'lic_end_date_singapore',
               'lic_start_date_india', 'lic_end_date_india']

newlicensedates = ['ID_Start_Date', 'ID_End_Date', 'TH_Start_Date', 'TH_End_Date', 
                   'PH_Start_Date', 'PH_End_Date', 'SG_Start_Date', 'SG_End_Date', 
                   'IN_Start_Date', 'IN_End_Date']

for i in country:
    country2 = i * 2 


#dropping unused columns

df.drop(['directors','lic_start_date_malaysia','lic_end_date_malaysia','lic_start_date_mauritius',
         'lic_end_date_mauritius','contenttype','status','playback_india','playback_philiphines','playback_thailand',
         'playback_singapore', 'playback_malaysia', 'playback_indonesia', 'download_india', 'download_philiphines', 
         'download_thailand', 'download_singapore', 'download_malaysia', 'download_indonesia', 'rating_india', 
         'rating_philiphines', 'rating_thailand', 'rating_singapore', 'rating_malaysia', 'rating_indonesia', 
         'cp_free_trial', 'hooq_free_trial', 'language_of_origin', 'extract_id', 'load_date', 'master_image_url', 
         'subtitles', 'source_url', 'availability_india', 'availability_philiphines', 'availability_thailand', 
         'availability_singapore', 'availability_malaysia', 'availability_indonesia', 'rental_india', 'rental_philiphines', 
         'rental_thailand', 'rental_singapore', 'rental_malaysia', 'rental_indonesia', 'productid_india', 
         'productid_philiphines', 'productid_thailand', 'productid_singapore', 'productid_malaysia', 'productid_indonesia', 
         'price_india', 'price_philiphines', 'price_thailand', 'price_singapore', 'price_malaysia', 'price_indonesia', 
         'rental_duration', 'currency_india', 'currency_philiphines', 'currency_thailand', 'currency_singapore', 
         'currency_malaysia', 'currency_indonesia'], axis=1, inplace=True)

#Creating new columns to capture the converted dates from excel's default

licensedates = ['lic_start_date_indonesia', 'lic_end_date_indonesia', 'lic_start_date_thailand', 'lic_end_date_thailand',
               'lic_start_date_philiphines', 'lic_end_date_philiphines', 'lic_start_date_singapore', 'lic_end_date_singapore',
               'lic_start_date_india', 'lic_end_date_india']

newlicensedates = ['ID_Start_Date', 'ID_End_Date', 'TH_Start_Date', 'TH_End_Date', 
                   'PH_Start_Date', 'PH_End_Date', 'SG_Start_Date', 'SG_End_Date', 
                   'IN_Start_Date', 'IN_End_Date']

for ld, nld in zip(licensedates, newlicensedates):
    df[nld] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df[ld], 'D')

newlicensedates_start = [s for s in newlicensedates if "Start" in s]
newlicensedates_end = [s for s in newlicensedates if "End" in s]

