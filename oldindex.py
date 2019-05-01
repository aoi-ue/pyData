import datetime as dt 
import pandas as pd
import numpy as np
import seaborn as sns
import xlrd
from string import Template

import plotly
plotly.tools.set_credentials_file(username='SandeepSingh', api_key='UnB6UI5RTJVMzzK4eQUx')
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import IFrame

from datetime import date
from dateutil.relativedelta import relativedelta

import matplotlib.pyplot as plt

def strip_spaces(a_str_with_spaces):
    return a_str_with_spaces.replace(' ', '')

excelname = 'x'

df = pd.read_csv(excelname,
                   converters = {'subtitle_english': strip_spaces, 'subtitle_bahasa': strip_spaces, 'subtitle_thai': strip_spaces, 
                                 'subtitle_hindi': strip_spaces, 'subtitle_tamil': strip_spaces, 'subtitle_telegu': strip_spaces, 
                                 'audiolanguage_english': strip_spaces, 'audiolanguage_hindi': strip_spaces, 
                                 'audiolanguage_tamil': strip_spaces, 'audiolanguage_telegu': strip_spaces, 
                                 'audiolanguage_thai': strip_spaces, 'audiolanguage_mandarin': strip_spaces, 
                                 'audiolanguage_bahasa': strip_spaces})
                                 

#setting a variable for 3 months
three_months = date.today() + relativedelta(months=+3)
mth3 = pd.to_datetime(three_months)

#Variable to get today's date automatically
todaydate = pd.datetime.now()

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

#Creating new columns to capture the converted dates from excel's default

df['ID_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_indonesia, 'D')
df['ID_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_indonesia, 'D')
df['TH_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_thailand, 'D')
df['TH_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_thailand, 'D')
df['PH_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_philiphines, 'D')
df['PH_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_philiphines, 'D')
df['SG_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_singapore, 'D')
df['SG_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_singapore, 'D')
df['IN_Start_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_start_date_india, 'D')
df['IN_End_Date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df.lic_end_date_india, 'D')

#Categorize Start_Dates into Current (currently running) or Future (to run in the future)
df['ID_TimePeriod'] = np.where(df['ID_Start_Date']<=todaydate, 'Current', 'Future')
df['TH_TimePeriod'] = np.where(df['TH_Start_Date']<=todaydate, 'Current', 'Future')
df['PH_TimePeriod'] = np.where(df['PH_Start_Date']<=todaydate, 'Current', 'Future')
df['SG_TimePeriod'] = np.where(df['SG_Start_Date']<=todaydate, 'Current', 'Future')
df['IN_TimePeriod'] = np.where(df['IN_Start_Date']<=todaydate, 'Current', 'Future')


#Categorize End_Dates into Expiring (within the next 3 months) or Not Expiring in the near future
df['ID_Expiring'] = np.where((df['ID_End_Date'] >= todaydate) & (df['ID_End_Date'] <= mth3), 'Expiring', 'Not Expiring')
df['TH_Expiring'] = np.where((df['TH_End_Date'] >= todaydate) & (df['TH_End_Date'] <= mth3), 'Expiring', 'Not Expiring')
df['PH_Expiring'] = np.where((df['PH_End_Date'] >= todaydate) & (df['PH_End_Date'] <= mth3), 'Expiring', 'Not Expiring')
df['SG_Expiring'] = np.where((df['SG_End_Date'] >= todaydate) & (df['SG_End_Date'] <= mth3), 'Expiring', 'Not Expiring')
df['IN_Expiring'] = np.where((df['IN_End_Date'] >= todaydate) & (df['IN_End_Date'] <= mth3), 'Expiring', 'Not Expiring')

#Categorize subtitles to Live or Not Live
df['ENG_SUB'] = np.where(df['subtitle_english'] == 'Y', 'Live', 'Not Live')
df['BH_SUB'] = np.where(df['subtitle_bahasa'] == 'Y', 'Live', 'Not Live')
df['TH_SUB'] = np.where(df['subtitle_thai'] == 'Y', 'Live', 'Not Live')
df['HIN_SUB'] = np.where(df['subtitle_hindi'] == 'Y', 'Live', 'Not Live')
df['TAM_SUB'] = np.where(df['subtitle_tamil'] == 'Y', 'Live', 'Not Live')
df['TEL_SUB'] = np.where(df['subtitle_telegu'] == 'Y', 'Live', 'Not Live')

#Categorize dubs to Live or Not Live
df['BH_DUB'] = np.where(df['audiolanguage_bahasa'] == 'Y', 'Live', 'Not Live')
df['TH_DUB'] = np.where(df['audiolanguage_thai'] == 'Y', 'Live', 'Not Live')
df['MAN_DUB'] = np.where(df['audiolanguage_mandarin'] == 'Y', 'Live', 'Not Live')
df['HIN_DUB'] = np.where(df['audiolanguage_hindi'] == 'Y', 'Live', 'Not Live')
df['TAM_DUB'] = np.where(df['audiolanguage_tamil'] == 'Y', 'Live', 'Not Live')
df['TEL_DUB'] = np.where(df['audiolanguage_telegu'] == 'Y', 'Live', 'Not Live')

#TOTALS, excludes expired content
ID_SVOD_TOTALDURATION = df[(df['vod_type'] == 'SVOD') & (df['ID_End_Date'] >= todaydate)]['duration'].sum()
TH_SVOD_TOTALDURATION = df[(df['vod_type'] == 'SVOD') & (df['TH_End_Date'] >= todaydate)]['duration'].sum()
PH_SVOD_TOTALDURATION = df[(df['vod_type'] == 'SVOD') & (df['PH_End_Date'] >= todaydate)]['duration'].sum()
SG_SVOD_TOTALDURATION = df[(df['vod_type'] == 'SVOD') & (df['SG_End_Date'] >= todaydate)]['duration'].sum()
IN_SVOD_TOTALDURATION = df[(df['vod_type'] == 'SVOD') & (df['IN_End_Date'] >= todaydate)]['duration'].sum()

COUNTRY_SVOD = [ID_SVOD_TOTALDURATION, TH_SVOD_TOTALDURATION, PH_SVOD_TOTALDURATION, SG_SVOD_TOTALDURATION, IN_SVOD_TOTALDURATION]

ID_TVOD_TOTALDURATION = df[(df['vod_type'] == 'TVOD') & (df['ID_End_Date'] >= todaydate)]['duration'].sum()
TH_TVOD_TOTALDURATION = df[(df['vod_type'] == 'TVOD') & (df['TH_End_Date'] >= todaydate)]['duration'].sum()
PH_TVOD_TOTALDURATION = df[(df['vod_type'] == 'TVOD') & (df['PH_End_Date'] >= todaydate)]['duration'].sum()
SG_TVOD_TOTALDURATION = df[(df['vod_type'] == 'TVOD') & (df['SG_End_Date'] >= todaydate)]['duration'].sum()
IN_TVOD_TOTALDURATION = df[(df['vod_type'] == 'TVOD') & (df['IN_End_Date'] >= todaydate)]['duration'].sum()

COUNTRY_TVOD = [ID_TVOD_TOTALDURATION, TH_TVOD_TOTALDURATION, PH_TVOD_TOTALDURATION, SG_TVOD_TOTALDURATION, IN_TVOD_TOTALDURATION]