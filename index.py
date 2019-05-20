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

excelname = 'x'

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

#Setting main lists and string format

country = ['indonesia', 'thailand', 'philiphines', 'singapore', 'india']
countrycode = ['ID', 'TH', 'PH', 'SG', 'IN']
sublanguage = ['english', 'bahasa', 'thai', 'hindi', 'tamil', 'telegu']
audiolanguage = ['english', 'bahasa', 'thai', 'mandarin', 'hindi', 'tamil', 'telegu']
subcode = ['ENG', 'BH', 'TH', 'HIN', 'TAM', 'TEL']
audiocode = ['ENG', 'BH', 'TH', 'MAN', 'HIN', 'TAM' ,'TEL']

subtext = "subtitle_"
dubtext = "audiolanguage_"
oldstartlic = "lic_start_date_"
oldendlic = "lic_end_date_"
newstartlic = "_Start_Date"
newendlic = "_End_Date"
tp = "_TimePeriod"
ccexp = "_Expiring"
ccsub = "_SUB"
ccdub = "_DUB"

subtitlelist = []
audiolist = []
oldstartliclist = []
oldendliclist = []
newstartliclist = []
newendliclist = []
newtp = []
newccexp = []
newccsub = []
newccdub = []

#########################################################################################################

for a, b in zip(sublanguage, audiolanguage):
    subtitlelist.append(subtext + a)
    audiolist.append(dubtext + b)
    
for c in country:
    oldstartliclist.append(oldstartlic + c)
    oldendliclist.append(oldendlic + c)
    
for cc in countrycode:
    newstartliclist.append(cc + newstartlic)
    newendliclist.append(cc + newendlic)
    newtp.append(cc + tp)
    newccexp.append(cc + ccexp)
    
for sc in subcode:
    newccsub.append(sc + ccsub)
    
for ac in audiocode:
    newccdub.append(ac + ccdub)

subtitleaudiolist = subtitlelist + audiolist
oldstartend = oldstartliclist + oldendliclist
newstartend = newstartliclist + newendliclist

#########################################################################################################

#Removing whitespaces from every column included in subtitleaudiolist

for i in subtitleaudiolist:
    df[i] = df[i].str.strip()

#Converting the old date columns into new date columns with the excel date being converted to readable dates

for old, new in zip(oldstartend, newstartend):
    df[new] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df[old], 'D')

for d, e in zip(newtp, newstartliclist):
    df[d] = np.where(df[e]<=todaydate, 'Current', 'Future')
    
#Categorize Start_Dates into Current (currently running) or Future (to run in the future)
    
for f, g in zip(newtp, newstartliclist):
    df[f] = np.where(df[g]<=todaydate, 'Current', 'Future')
    
#Categorize End_Dates into Expiring (within the next 3 months) or Not Expiring in the near future

for h, i in zip(newccexp, newendliclist):
    df[h] = np.where((df[i] >= todaydate) & (df[i] <= mth3), 'Expiring', 'Not Expiring')
    
#Categorize subtitles to Live or Not Live

for j, k in zip(newccsub, subtitlelist):
    df[j] = np.where(df[k] == 'Y', 'Live', 'Not Live')
    
#Categorize dubs to Live or Not Live

for l, m in zip(newccdub, audiolist):
    df[l] = np.where(df[m] == 'Y', 'Live', 'Not Live')

