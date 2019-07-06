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

#########################################################################################################
#Capturing the total hours for SVOD and TVOD

svod_td = [df[(df['vod_type'] == 'SVOD') & (df[i] >= todaydate)]['duration'].sum() for i in new_end_lic_list]
tvod_td = [df[(df['vod_type'] == 'TVOD') & (df[i] >= todaydate)]['duration'].sum() for i in new_end_lic_list]

#Creating separate data frames for the individual countries

svemp = []
tvemp = []

for i in old_end_lic_list:
    svemp.append(df[(df['vod_type'] == 'SVOD') & (df[i] >= todaydate)])
    
for i in old_end_lic_list:
    tvemp.append(df[(df['vod_type'] == 'TVOD') & (df[i] >= todaydate)])

ID_svoddf = svemp[0]
TH_svoddf = svemp[1]
PH_svoddf = svemp[2]
SG_svoddf = svemp[3]
IN_svoddf = svemp[4]

ID_tvoddf = tvemp[0]
TH_tvoddf = tvemp[1]
PH_tvoddf = tvemp[2]
SG_tvoddf = tvemp[3]
IN_tvoddf = tvemp[4]




### ID Hours

indo_sub_dub_list = ['ENG_SUB', 'BH_SUB', 'BH_DUB']
indo_svod_emp_list = []
indo_tvod_emp_list = []

for i in indo_sub_dub_list:
    a = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Current') & (ID_svoddf[i] == 'Live')]['duration'].sum()
    b = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Future') & (ID_svoddf[i] == 'Live')]['duration'].sum()
    c = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Current') & (ID_svoddf[i] == 'Not Live')]['duration'].sum()
    d = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Future') & (ID_svoddf[i] == 'Not Live')]['duration'].sum()
    e = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Expiring') & (ID_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Current') & (ID_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Future') & (ID_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Current') & (ID_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Future') & (ID_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = ID_tvoddf[(ID_tvoddf['ID_Expiring'] == 'Expiring') & (ID_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    indo_svod_emp_list.append(total)
    indo_tvod_emp_list.append(total2)

### TH Hours

thai_sub_dub_list = ['ENG_SUB', 'TH_SUB', 'TH_DUB']
thai_svod_emp_list = []
thai_tvod_emp_list = []

for i in thai_sub_dub_list:
    a = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Current') & (TH_svoddf[i] == 'Live')]['duration'].sum()
    b = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Future') & (TH_svoddf[i] == 'Live')]['duration'].sum()
    c = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Current') & (TH_svoddf[i] == 'Not Live')]['duration'].sum()
    d = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Future') & (TH_svoddf[i] == 'Not Live')]['duration'].sum()
    e = TH_svoddf[(TH_svoddf['TH_Expiring'] == 'Expiring') & (TH_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Current') & (TH_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Future') & (TH_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Current') & (TH_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Future') & (TH_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = TH_tvoddf[(TH_tvoddf['TH_Expiring'] == 'Expiring') & (TH_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    thai_svod_emp_list.append(total)
    thai_tvod_emp_list.append(total2)

### PH HOURS

ph_sub_dub_list = ['ENG_SUB']
ph_svod_emp_list = []
ph_tvod_emp_list = []

for i in ph_sub_dub_list:
    a = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Current') & (PH_svoddf[i] == 'Live')]['duration'].sum()
    b = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Future') & (PH_svoddf[i] == 'Live')]['duration'].sum()
    c = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Current') & (PH_svoddf[i] == 'Not Live')]['duration'].sum()
    d = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Future') & (PH_svoddf[i] == 'Not Live')]['duration'].sum()
    e = PH_svoddf[(PH_svoddf['PH_Expiring'] == 'Expiring') & (PH_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Current') & (PH_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Future') & (PH_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Current') & (PH_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Future') & (PH_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = PH_tvoddf[(PH_tvoddf['PH_Expiring'] == 'Expiring') & (PH_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    ph_svod_emp_list.append(total)
    ph_tvod_emp_list.append(total2)

### SG HOURS

sg_sub_dub_list = ['ENG_SUB', 'MAN_DUB']
sg_svod_emp_list = []
sg_tvod_emp_list = []

for i in sg_sub_dub_list:
    a = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Current') & (SG_svoddf[i] == 'Live')]['duration'].sum()
    b = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Future') & (SG_svoddf[i] == 'Live')]['duration'].sum()
    c = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Current') & (SG_svoddf[i] == 'Not Live')]['duration'].sum()
    d = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Future') & (SG_svoddf[i] == 'Not Live')]['duration'].sum()
    e = SG_svoddf[(SG_svoddf['SG_Expiring'] == 'Expiring') & (SG_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Current') & (SG_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Future') & (SG_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Current') & (SG_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Future') & (SG_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = SG_tvoddf[(SG_tvoddf['SG_Expiring'] == 'Expiring') & (SG_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    sg_svod_emp_list.append(total)
    sg_tvod_emp_list.append(total2)

### IN HOURS

in_sub_dub_list = ['ENG_SUB', 'HIN_SUB', 'TAM_SUB', 'TEL_SUB', 'HIN_DUB', 'TAM_DUB', 'TEL_DUB']
in_svod_emp_list = []
in_tvod_emp_list = []

for i in in_sub_dub_list:
    a = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Current') & (IN_svoddf[i] == 'Live')]['duration'].sum()
    b = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Future') & (IN_svoddf[i] == 'Live')]['duration'].sum()
    c = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Current') & (IN_svoddf[i] == 'Not Live')]['duration'].sum()
    d = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Future') & (IN_svoddf[i] == 'Not Live')]['duration'].sum()
    e = IN_svoddf[(IN_svoddf['IN_Expiring'] == 'Expiring') & (IN_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Current') & (IN_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Future') & (IN_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Current') & (IN_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Future') & (IN_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = IN_tvoddf[(IN_tvoddf['IN_Expiring'] == 'Expiring') & (IN_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    in_svod_emp_list.append(total)
    in_tvod_emp_list.append(total2)

#SVOD Country Level Total Hours

def pie1(): 
    labels = ['ID SVOD', 'TH SVOD', 'PH_SVOD', 'SG_SVOD', 'IN_SVOD']
    values = svod_td
    colors = ['#822B24', '#1B4F6A', '#36614F', '#A94B35', '#571F4E']

    trace = go.Pie(labels=labels, values=values,
                   hoverinfo='label+value', textinfo='label+percent', 
                   textfont=dict(size=14),
                   marker=dict(colors=colors, 
                               line=dict(color='#000000', width=2)))

    return py.plot([trace], filename='styled_pie_chart')

#SVOD ID 5 Tier Hours

def bar1():

    trace1 = go.Bar(
        x=['Current Live', 'Future Live', 'Current Not Live', 'Future Not Live', 'Expiring'],
        y=indo_svod_emp_list[0],
        marker=dict(color='#4570ba'),
        name='ID ENG SUB'
    )

    trace2 = go.Bar(
        x=['Current Live', 'Future Live', 'Current Not Live', 'Future Not Live', 'Expiring'],
        y=indo_svod_emp_list[1],
        marker=dict(color='#ba4558'),
        name='ID BH SUB'
    )

    trace3 = go.Bar(
        x=['Current Live', 'Future Live', 'Current Not Live', 'Future Not Live', 'Expiring'],
        y=indo_svod_emp_list[1],
        marker=dict(color='#7e57a8'),
        name='ID BH DUB'
    )

    data = [trace1, trace2, trace3]
    layout = go.Layout(
        barmode='stack'
    )

    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig, filename='stacked-bar')


pie1()
bar1()