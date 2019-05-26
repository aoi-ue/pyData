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

excelname = 'E:\\PythonProjects\\pyData\\DataDump\\CSV_SINGTEL_INGESTION_EXTRACT_2018-12-26.csv'

#creating the dataframe, df

df = pd.read_csv(excelname)

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

###Creating 2 lists from country:

country = ['indonesia', 'thailand', 'philiphines', 'singapore', 'india']

str_old_start_lic = "lic_start_date_"
str_old_end_lic = "lic_end_date_"

old_start_lic_list = []
old_end_lic_list = []

for c in country:
    #lic_start_date_indonesia
    old_start_lic_list.append(str_old_start_lic + c)
    #lic_end_date_indonesia
    old_end_lic_list.append(str_old_end_lic + c)
    
#########################################################################################################
    
###Creating 4 lists from country_code:

country_code = ['ID', 'TH', 'PH', 'SG', 'IN']

str_new_start_lic = "_Start_Date"
str_new_end_lic = "_End_Date"
str_tp = "_TimePeriod"
str_ccexp = "_Expiring"

new_start_lic_list = []
new_end_lic_list = []
new_tp = []
new_ccexp = []

for cc in country_code:
    #ID_Start_Date
    new_start_lic_list.append(cc + str_new_start_lic)
    #ID_End_Date
    new_end_lic_list.append(cc + str_new_end_lic)
    #ID_TimePeriod
    new_tp.append(cc + str_tp)
    #ID_Expiring
    new_ccexp.append(cc + str_ccexp)

#########################################################################################################
    
###Creating 2 lists from sub_language & audio_language

sub_language = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu']
audio_language = ['english', 'bahasa', 'thai', 'mandarin', 'hindi', 'tamil', 'telegu']

str_sub_text = "subtitle_"
str_dub_text = "audiolanguage_"

subtitle_list = []
audio_list = []

for a, b in zip(sub_language, audio_language):
    #subtitle_english
    subtitle_list.append(str_sub_text + a)
    #audiolanguage_english
    audio_list.append(str_dub_text + b)

#########################################################################################################
    
###Creating 1 list from sub_code & audio_code

sub_code = ['ENG', 'BH', 'TH', 'HIN', 'TAM', 'TEL']
audio_code = ['ENG', 'BH', 'TH', 'MAN', 'HIN', 'TAM' ,'TEL']

str_ccsub = "_SUB"
str_ccdub = "_DUB"

new_ccsub_list = []
new_ccdub_list = []
    
for sc, ac in zip(sub_code,audio_code):
    #ENG_SUB
    new_ccsub_list.append(sc + str_ccsub)
    #ENG_DUB
    new_ccdub_list.append(ac + str_ccdub)

#########################################################################################################

### Combining 2 lists into 1

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

for new, con in zip(new_ccsub_list, subtitle_list):
    df[new] = np.where(df[con] == 'Y', 'Live', 'Not Live')
    
#Categorize dubs to Live or Not Live

for new, con in zip(new_ccdub_list, audio_list):
    df[new] = np.where(df[con] == 'Y', 'Live', 'Not Live')