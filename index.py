import datetime as dt 
import pandas as pd
import numpy as np
import xlrd
from datetime import date
from dateutil.relativedelta import relativedelta

def strip_spaces(a_str_with_spaces):
    return a_str_with_spaces.replace(' ', '')

#we will replace this with version control excel

excelname = 'XXX'

df = pd.read_excel(excelname, sheet_name = 'Sheet1',
                  converters={'subtitle_english': strip_spaces, 'subtitle_bahasa': strip_spaces, 'subtitle_thai': strip_spaces,
                             'subtitle_hindi': strip_spaces, 'subtitle_tamil': strip_spaces, 'subtitle_telegu': strip_spaces,
                             'audiolanguage_english': strip_spaces, 'audiolanguage_hindi': strip_spaces,
                             'audiolanguage_tamil': strip_spaces, 'audiolanguage_telegu': strip_spaces,
                             'audiolanguage_thai': strip_spaces, 'audiolanguage_mandarin': strip_spaces,
                             'audiolanguage_bahasa': strip_spaces})

#setting a variable for 3 months
three_months = date.today() + relativedelta(months=+3)
mth3 = pd.to_datetime(three_months)

#Deleting unused columns

df.drop(['locale','directors','lic_start_date_malaysia','lic_end_date_malaysia','lic_start_date_mauritius',
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

#Converting the dates

#Indonesia
df['ID_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_indonesia, 'D')
df['ID_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_indonesia, 'D')

#Thailand
df['TH_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_thailand, 'D')
df['TH_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_thailand, 'D')

#Philippines
df['PH_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_philiphines, 'D')
df['PH_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_philiphines, 'D')

#Singapore
df['SG_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_singapore, 'D')
df['SG_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_singapore, 'D')

#India
df['IN_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_india, 'D')
df['IN_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_india, 'D')

#Splitting the dataset into S & T

dfS = df[df['vod_type'] == 'SVOD']
dfT = df[df['vod_type'] == 'TVOD']

#Variable to get today's date automatically
todaydate = pd.datetime.now()