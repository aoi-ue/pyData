import datetime as dt 
from datetime import date
from dateutil.relativedelta import relativedelta

import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from string import Template

from s3 import df

# excelname = ''

#Test2: Ensure that file name has csv

# def inputdata():
#     df = pd.read_csv(excelname)
#     return df

#Test3: Ensure that df is not empty
# df = inputdata()

#setting a variable for 3 months
three_months = date.today() + relativedelta(months=+3)
mth3 = pd.to_datetime(three_months)

#creating a variable called todaydate to capture today's date
todaydate = pd.datetime.now()

#drop columns
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

#Converting the dates into a datetime format

df['lic_end_date_indonesia'] = pd.to_datetime(df.lic_end_date_indonesia)
df['lic_end_date_thailand'] = pd.to_datetime(df.lic_end_date_thailand)
df['lic_end_date_philiphines'] = pd.to_datetime(df.lic_end_date_philiphines)
df['lic_end_date_singapore'] = pd.to_datetime(df.lic_end_date_singapore)
df['lic_end_date_india'] = pd.to_datetime(df.lic_end_date_india)

df['lic_start_date_indonesia'] = pd.to_datetime(df.lic_start_date_indonesia)
df['lic_start_date_thailand'] = pd.to_datetime(df.lic_start_date_thailand)
df['lic_start_date_philiphines'] = pd.to_datetime(df.lic_start_date_philiphines)
df['lic_start_date_singapore'] = pd.to_datetime(df.lic_start_date_singapore)
df['lic_start_date_india'] = pd.to_datetime(df.lic_start_date_india)

#Setting up name/list variables

country = ['indonesia', 'thailand', 'philiphines', 'singapore', 'india']
country_code = ['ID', 'TH', 'PH', 'SG', 'IN']
sub_language = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu']
audio_language = ['english', 'bahasa', 'thai', 'mandarin', 'hindi', 'tamil', 'telegu']
sub_code = ['ENG', 'BH', 'TH', 'HIN', 'TAM', 'TEL']
audio_code = ['ENG', 'BH', 'TH', 'MAN', 'HIN', 'TAM' ,'TEL']

old_start_lic_list = ["lic_start_date_"+ i for i in country]
old_end_lic_list = ["lic_end_date_" + i for i in country]
new_start_lic_list = [i + "_Start_Date" for i in country_code]
new_end_lic_list = [i + "_End_Date" for i in country_code]
new_tp = [i + "_TimePeriod" for i in country_code]
new_ccexp = [i + "_Expiring" for i in country_code]
subtitle_list = ["subtitle_" + i for i in sub_language]
audio_list = ["audiolanguage_" + i for i in audio_language]
new_ccsub_list = [i + "_SUB" for i in sub_code]
new_ccdub_list = [i + "_DUB" for i in audio_code]

#########################################################################################################

subtitle_audio_list = subtitle_list + audio_list
old_start_end = old_start_lic_list + old_end_lic_list
new_start_end = new_start_lic_list + new_end_lic_list

#########################################################################################################

#Removing whitespaces from every column included in subtitleaudiolist

for i in subtitle_audio_list:
    df[i] = df[i].str.strip()
    
#Categorize Start_Dates into Current (currently running) or Future (to run in the future)
    
for new, con in zip(new_tp, new_start_lic_list):
    df[new] = np.where(df[con]<=todaydate, 'Current', 'Future')
    
#Categorize End_Dates into Expiring (within the next 3 months) or Not Expiring in the near future

for new, con in zip(new_ccexp, new_end_lic_list):
    df[new] = np.where((df[con] >= todaydate) & (df[con] <= mth3), 'Expiring', 'Not Expiring')
    
#Categorize subtitles to Live or Not Live

for new1, con1 in zip(new_ccsub_list, subtitle_list):
    df[new1] = np.where(df[con1] == 'Y', 'Live', 'Not Live')

#Categorize dubs to Live or Not Live
    
for new2, con2 in zip(new_ccdub_list, audio_list):
    df[new2] = np.where(df[con2] == 'Y', 'Live', 'Not Live')