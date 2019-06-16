import datetime as dt 
from datetime import date
from dateutil.relativedelta import relativedelta

import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from string import Template

import plotly
plotly.tools.set_credentials_file(username='SandeepSingh', api_key='UnB6UI5RTJVMzzK4eQUx')
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import IFrame

#Test2: Ensure that file name has csv
excelname = 'E:\\PythonProjects\\pyData\\DataDump\\MOCK_SINGTEL_INGESTION_EXTRACT_2018-12-26.csv'

def inputdata():
    df = pd.read_csv(excelname)
    return df

#Test3: Ensure that df is not empty
df = inputdata()

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

#Converting the old date columns into new date columns with the excel date being converted to readable dates

for new, old in zip(new_start_end, old_start_end):
    df[new] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df[old], 'D')
    
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

#########################################################################################################
#Capturing the total hours for SVOD and TVOD

svod_td = [df[(df['vod_type'] == 'SVOD') & (df[i] >= todaydate)]['duration'].sum() for i in new_end_lic_list]
tvod_td = [df[(df['vod_type'] == 'TVOD') & (df[i] >= todaydate)]['duration'].sum() for i in new_end_lic_list]

### ID Hours

indo_sub_dub_list = ['ENG_SUB', 'BH_SUB', 'BH_DUB']
indo_svod_emp_list = []

for i in indo_sub_dub_list:
    a = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df[i] == 'Live')]['duration'].sum()
    b = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df[i] == 'Live')]['duration'].sum()
    c = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df[i] == 'Not Live')]['duration'].sum()
    d = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df[i] == 'Not Live')]['duration'].sum()
    e = df[(df['vod_type'] == 'SVOD') & (df['ID_Expiring'] == 'Expiring') & (df[i] == 'Not Live')]['duration'].sum()
    total = [a, b, c, d, e]
    indo_svod_emp_list.append(total)

### TH Hours

thai_sub_dub_list = ['ENG_SUB', 'TH_SUB', 'TH_DUB']
thai_svod_emp_list = []

for i in thai_sub_dub_list:
    a = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df[i] == 'Live')]['duration'].sum()
    b = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df[i] == 'Live')]['duration'].sum()
    c = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df[i] == 'Not Live')]['duration'].sum()
    d = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df[i] == 'Not Live')]['duration'].sum()
    e = df[(df['vod_type'] == 'SVOD') & (df['TH_Expiring'] == 'Expiring') & (df[i] == 'Not Live')]['duration'].sum()
    total = [a, b, c, d, e]
    thai_svod_emp_list.append(total)

### PH HOURS

ph_sub_dub_list = ['ENG_SUB']
ph_svod_emp_list = []

for i in ph_sub_dub_list:
    a = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Current') & (df[i] == 'Live')]['duration'].sum()
    b = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Future') & (df[i] == 'Live')]['duration'].sum()
    c = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Current') & (df[i] == 'Not Live')]['duration'].sum()
    d = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Future') & (df[i] == 'Not Live')]['duration'].sum()
    e = df[(df['vod_type'] == 'SVOD') & (df['PH_Expiring'] == 'Expiring') & (df[i] == 'Not Live')]['duration'].sum()
    total = [a, b, c, d, e]
    ph_svod_emp_list.append(total)

### SG HOURS

sg_sub_dub_list = ['ENG_SUB', 'MAN_DUB']
sg_svod_emp_list = []

for i in sg_sub_dub_list:

    a = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Current') & (df[i] == 'Live')]['duration'].sum()
    b = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Future') & (df[i] == 'Live')]['duration'].sum()
    c = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Current') & (df[i] == 'Not Live')]['duration'].sum()
    d = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Future') & (df[i] == 'Not Live')]['duration'].sum()
    e = df[(df['vod_type'] == 'SVOD') & (df['SG_Expiring'] == 'Expiring') & (df[i] == 'Not Live')]['duration'].sum()
    total = [a, b, c, d, e]
    sg_svod_emp_list.append(total)

### IN HOURS

in_sub_dub_list = ['ENG_SUB', 'HIN_SUB', 'TAM_SUB', 'TEL_SUB', 'HIN_DUB', 'TAM_DUB', 'TEL_DUB']
in_svod_emp_list = []

for i in in_sub_dub_list:
    a = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df[i] == 'Live')]['duration'].sum()
    b = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df[i] == 'Live')]['duration'].sum()
    c = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df[i] == 'Not Live')]['duration'].sum()
    d = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df[i] == 'Not Live')]['duration'].sum()
    e = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df[i] == 'Not Live')]['duration'].sum()
    total = [a, b, c, d, e]
    in_svod_emp_list.append(total)

print("works")