import datetime as dt 
import pandas as pd
import numpy as np
import xlrd
from datetime import date
from dateutil.relativedelta import relativedelta

def strip_spaces(a_str_with_spaces):
    return a_str_with_spaces.replace(' ', '')

#we will replace this with version control excel
df = pd.read_excel('', sheet_name = 'Sheet1',
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

################################################ S ################################################

#Removing Expired Content by taking License End Date >= Today's Date

#Indonesia
dfS_ID = dfS[dfS['ID_End_Date'] >= todaydate]

#Thailand
dfS_TH = dfS[dfS['TH_End_Date'] >= todaydate]

#Philippines
dfS_PH = dfS[dfS['PH_End_Date'] >= todaydate]

#Singapore
dfS_SG = dfS[dfS['SG_End_Date'] >= todaydate]

#India
dfS_IN = dfS[dfS['IN_End_Date'] >= todaydate]

################################################ S INDONESIA ################################################

#BAHASA CURRENT + LIVE
dfS_ID_CL = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['subtitle_bahasa'] == 'Y')]

#BAHASA FUTURE + LIVE
dfS_ID_FL = dfS_ID[(dfS_ID['ID_Start_Date'] > todaydate) & (dfS_ID['subtitle_bahasa'] == 'Y')]

#BAHASA CURRENT + NOT LIVE
dfS_ID_CN = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['subtitle_bahasa'] == 'N')]

#BAHASA FUTURE + NOT LIVE
dfS_ID_FN = dfS_ID[(dfS_ID['ID_Start_Date'] > todaydate) & (dfS_ID['subtitle_bahasa'] == 'N')]

#BAHASA EXPIRING
dfS_ID_EXP = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['subtitle_bahasa'] == 'N') & 
                   (dfS_ID['ID_End_Date'] <= mth3)]

#############################################################################################################

#INDONESIA ENGLISH CURRENT + LIVE
dfS_IDE_CL = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['subtitle_english'] == 'Y')]

#INDONESIA ENGLISH FUTURE + LIVE
dfS_IDE_FL = dfS_ID[(dfS_ID['ID_Start_Date'] > todaydate) & (dfS_ID['subtitle_english'] == 'Y')]

#INDONESIA ENGLISH CURRENT + NOT LIVE
dfS_IDE_CN = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['subtitle_english'] == 'N')]

#INDONESIA ENGLISH FUTURE + NOT LIVE
dfS_IDE_FN = dfS_ID[(dfS_ID['ID_Start_Date'] > todaydate) & (dfS_ID['subtitle_english'] == 'N')]

#INDONESIA ENGLISH EXPIRING
dfS_IDE_EXP = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['subtitle_english'] == 'N') & 
                   (dfS_ID['ID_End_Date'] <= mth3)]

################################################ S THAILAND ################################################

#THAI CURRENT + LIVE
dfS_TH_CL = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['subtitle_thai'] == 'Y')]

#THAI FUTURE + LIVE
dfS_TH_FL = dfS_TH[(dfS_TH['TH_Start_Date'] > todaydate) & (dfS_TH['subtitle_thai'] == 'Y')]

#THAI CURRENT + NOT LIVE
dfS_TH_CN = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['subtitle_thai'] == 'N')]

#THAI FUTURE + NOT LIVE
dfS_TH_FN = dfS_TH[(dfS_TH['TH_Start_Date'] > todaydate) & (dfS_TH['subtitle_thai'] == 'N')]

#THAI EXPIRING
dfS_TH_EXP = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['subtitle_thai'] == 'N') & 
                   (dfS_TH['TH_End_Date'] <= mth3)]

#############################################################################################################

#THAI ENGLISH CURRENT + LIVE
dfS_THE_CL = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['subtitle_english'] == 'Y')]

#THAI ENGLISH FUTURE + LIVE
dfS_THE_FL = dfS_TH[(dfS_TH['TH_Start_Date'] > todaydate) & (dfS_TH['subtitle_english'] == 'Y')]

#THAI ENGLISH CURRENT + NOT LIVE
dfS_THE_CN = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['subtitle_english'] == 'N')]

#THAI ENGLISH FUTURE + NOT LIVE
dfS_THE_FN = dfS_TH[(dfS_TH['TH_Start_Date'] > todaydate) & (dfS_TH['subtitle_english'] == 'N')]

#THAI ENGLISH EXPIRING
dfS_THE_EXP = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['subtitle_english'] == 'N') & 
                   (dfS_TH['TH_End_Date'] <= mth3)]

################################################ S PHILIPPINES ################################################

#PHILIPPINES ENGLISH CURRENT + LIVE
dfS_PHE_CL = dfS_PH[(dfS_PH['PH_Start_Date'] <= todaydate) & (dfS_PH['subtitle_english'] == 'Y')]

#PHILIPPINES ENGLISH FUTURE + LIVE
dfS_PHE_FL = dfS_PH[(dfS_PH['PH_Start_Date'] > todaydate) & (dfS_PH['subtitle_english'] == 'Y')]

#PHILIPPINES ENGLISH CURRENT + NOT LIVE
dfS_PHE_CN = dfS_PH[(dfS_PH['PH_Start_Date'] <= todaydate) & (dfS_PH['subtitle_english'] == 'N')]

#PHILIPPINES ENGLISH FUTURE + NOT LIVE
dfS_PHE_FN = dfS_PH[(dfS_PH['PH_Start_Date'] > todaydate) & (dfS_PH['subtitle_english'] == 'N')]

#PHILIPPINES ENGLISH EXPIRING
dfS_PHE_EXP = dfS_PH[(dfS_PH['PH_Start_Date'] <= todaydate) & (dfS_PH['subtitle_english'] == 'N') & 
                   (dfS_PH['PH_End_Date'] <= mth3)]

################################################ S SINGAPORE ################################################

#SINGAPORE ENGLISH CURRENT + LIVE
dfS_SGE_CL = dfS_SG[(dfS_SG['SG_Start_Date'] <= todaydate) & (dfS_SG['subtitle_english'] == 'Y')]

#SINGAPORE ENGLISH FUTURE + LIVE
dfS_SGE_FL = dfS_SG[(dfS_SG['SG_Start_Date'] > todaydate) & (dfS_SG['subtitle_english'] == 'Y')]

#SINGAPORE ENGLISH CURRENT + NOT LIVE
dfS_SGE_CN = dfS_SG[(dfS_SG['SG_Start_Date'] <= todaydate) & (dfS_SG['subtitle_english'] == 'N')]

#SINGAPORE ENGLISH FUTURE + NOT LIVE
dfS_SGE_FN = dfS_SG[(dfS_SG['SG_Start_Date'] > todaydate) & (dfS_SG['subtitle_english'] == 'N')]

#SINGAPORE ENGLISH EXPIRING
dfS_SGE_EXP = dfS_SG[(dfS_SG['SG_Start_Date'] <= todaydate) & (dfS_SG['subtitle_english'] == 'N') & 
                   (dfS_SG['SG_End_Date'] <= mth3)]

################################################ S INDIA ################################################

#INDIA ENGLISH CURRENT + LIVE
dfS_INE_CL = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_english'] == 'Y')]

#INDIA ENGLISH FUTURE + LIVE
dfS_INE_FL = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_english'] == 'Y')]

#INDIA ENGLISH CURRENT + NOT LIVE
dfS_INE_CN = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_english'] == 'N')]

#INDIA ENGLISH FUTURE + NOT LIVE
dfS_INE_FN = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_english'] == 'N')]

#INDIA ENGLISH EXPIRING
dfS_INE_EXP = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_english'] == 'N') & 
                   (dfS_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA HINDI CURRENT + LIVE
dfS_INH_CL = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_hindi'] == 'Y')]

#INDIA HINDI FUTURE + LIVE
dfS_INH_FL = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_hindi'] == 'Y')]

#INDIA HINDI CURRENT + NOT LIVE
dfS_INH_CN = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_hindi'] == 'N')]

#INDIA HINDI FUTURE + NOT LIVE
dfS_INH_FN = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_hindi'] == 'N')]

#INDIA HINDI EXPIRING
dfS_INH_EXP = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_hindi'] == 'N') & 
                   (dfS_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TAMIL CURRENT + LIVE
dfS_INTA_CL = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_tamil'] == 'Y')]

#INDIA TAMIL FUTURE + LIVE
dfS_INTA_FL = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_tamil'] == 'Y')]

#INDIA TAMIL CURRENT + NOT LIVE
dfS_INTA_CN = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_tamil'] == 'N')]

#INDIA TAMIL FUTURE + NOT LIVE
dfS_INTA_FN = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_tamil'] == 'N')]

#INDIA TAMIL EXPIRING
dfS_INTA_EXP = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_tamil'] == 'N') & 
                   (dfS_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TELEGU CURRENT + LIVE
dfS_INTE_CL = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_telegu'] == 'Y')]

#INDIA TELEGU FUTURE + LIVE
dfS_INTE_FL = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_telegu'] == 'Y')]

#INDIA TELEGU CURRENT + NOT LIVE
dfS_INTE_CN = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_telegu'] == 'N')]

#INDIA TELEGU FUTURE + NOT LIVE
dfS_INTE_FN = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['subtitle_telegu'] == 'N')]

#INDIA TELEGU EXPIRING
dfS_INTE_EXP = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['subtitle_telegu'] == 'N') & 
                   (dfS_IN['IN_End_Date'] <= mth3)]


################################################ T ################################################

#Filtering vod_type for TVOD by Country
#Indonesia
dfT_ID = dfT[dfT['ID_End_Date'] >= todaydate]

#Thailand
dfT_TH = dfT[dfT['TH_End_Date'] >= todaydate]

#Philippines
dfT_PH = dfT[dfT['PH_End_Date'] >= todaydate]

#Singapore
dfT_SG = dfT[dfT['SG_End_Date'] >= todaydate]

#India
dfT_IN = dfT[dfT['IN_End_Date'] >= todaydate]

################################################ T INDONESIA ################################################

#BAHASA CURRENT + LIVE
dfT_ID_CL = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['subtitle_bahasa'] == 'Y')]

#BAHASA FUTURE + LIVE
dfT_ID_FL = dfT_ID[(dfT_ID['ID_Start_Date'] > todaydate) & (dfT_ID['subtitle_bahasa'] == 'Y')]

#BAHASA CURRENT + NOT LIVE
dfT_ID_CN = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['subtitle_bahasa'] == 'N')]

#BAHASA FUTURE + NOT LIVE
dfT_ID_FN = dfT_ID[(dfT_ID['ID_Start_Date'] > todaydate) & (dfT_ID['subtitle_bahasa'] == 'N')]

#BAHASA EXPIRING
dfT_ID_EXP = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['subtitle_bahasa'] == 'N') & 
                   (dfT_ID['ID_End_Date'] <= mth3)]

#############################################################################################################

#INDONESIA ENGLISH CURRENT + LIVE
dfT_IDE_CL = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['subtitle_english'] == 'Y')]

#INDONESIA ENGLISH FUTURE + LIVE
dfT_IDE_FL = dfT_ID[(dfT_ID['ID_Start_Date'] > todaydate) & (dfT_ID['subtitle_english'] == 'Y')]

#INDONESIA ENGLISH CURRENT + NOT LIVE
dfT_IDE_CN = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['subtitle_english'] == 'N')]

#INDONESIA ENGLISH FUTURE + NOT LIVE
dfT_IDE_FN = dfT_ID[(dfT_ID['ID_Start_Date'] > todaydate) & (dfT_ID['subtitle_english'] == 'N')]

#INDONESIA ENGLISH EXPIRING
dfT_IDE_EXP = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['subtitle_english'] == 'N') & 
                   (dfT_ID['ID_End_Date'] <= mth3)]

################################################ T THAILAND ################################################

#THAI CURRENT + LIVE
dfT_TH_CL = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['subtitle_thai'] == 'Y')]

#THAI FUTURE + LIVE
dfT_TH_FL = dfT_TH[(dfT_TH['TH_Start_Date'] > todaydate) & (dfT_TH['subtitle_thai'] == 'Y')]

#THAI CURRENT + NOT LIVE
dfT_TH_CN = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['subtitle_thai'] == 'N')]

#THAI FUTURE + NOT LIVE
dfT_TH_FN = dfT_TH[(dfT_TH['TH_Start_Date'] > todaydate) & (dfT_TH['subtitle_thai'] == 'N')]

#THAI EXPIRING
dfT_TH_EXP = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['subtitle_thai'] == 'N') & 
                   (dfT_TH['TH_End_Date'] <= mth3)]

#############################################################################################################

#THAI ENGLISH CURRENT + LIVE
dfT_THE_CL = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['subtitle_english'] == 'Y')]

#THAI ENGLISH FUTURE + LIVE
dfT_THE_FL = dfT_TH[(dfT_TH['TH_Start_Date'] > todaydate) & (dfT_TH['subtitle_english'] == 'Y')]

#THAI ENGLISH CURRENT + NOT LIVE
dfT_THE_CN = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['subtitle_english'] == 'N')]

#THAI ENGLISH FUTURE + NOT LIVE
dfT_THE_FN = dfT_TH[(dfT_TH['TH_Start_Date'] > todaydate) & (dfT_TH['subtitle_english'] == 'N')]

#THAI ENGLISH EXPIRING
dfT_THE_EXP = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['subtitle_english'] == 'N') & 
                   (dfT_TH['TH_End_Date'] <= mth3)]

################################################ T PHILIPPINES ################################################

#PHILIPPINES ENGLISH CURRENT + LIVE
dfT_PHE_CL = dfT_PH[(dfT_PH['PH_Start_Date'] <= todaydate) & (dfT_PH['subtitle_english'] == 'Y')]

#PHILIPPINES ENGLISH FUTURE + LIVE
dfT_PHE_FL = dfT_PH[(dfT_PH['PH_Start_Date'] > todaydate) & (dfT_PH['subtitle_english'] == 'Y')]

#PHILIPPINES ENGLISH CURRENT + NOT LIVE
dfT_PHE_CN = dfT_PH[(dfT_PH['PH_Start_Date'] <= todaydate) & (dfT_PH['subtitle_english'] == 'N')]

#PHILIPPINES ENGLISH FUTURE + NOT LIVE
dfT_PHE_FN = dfT_PH[(dfT_PH['PH_Start_Date'] > todaydate) & (dfT_PH['subtitle_english'] == 'N')]

#PHILIPPINES ENGLISH EXPIRING
dfT_PHE_EXP = dfT_PH[(dfT_PH['PH_Start_Date'] <= todaydate) & (dfT_PH['subtitle_english'] == 'N') & 
                   (dfT_PH['PH_End_Date'] <= mth3)]

################################################ T SINGAPORE ################################################

#SINGAPORE ENGLISH CURRENT + LIVE
dfT_SGE_CL = dfT_SG[(dfT_SG['SG_Start_Date'] <= todaydate) & (dfT_SG['subtitle_english'] == 'Y')]

#SINGAPORE ENGLISH FUTURE + LIVE
dfT_SGE_FL = dfT_SG[(dfT_SG['SG_Start_Date'] > todaydate) & (dfT_SG['subtitle_english'] == 'Y')]

#SINGAPORE ENGLISH CURRENT + NOT LIVE
dfT_SGE_CN = dfT_SG[(dfT_SG['SG_Start_Date'] <= todaydate) & (dfT_SG['subtitle_english'] == 'N')]

#SINGAPORE ENGLISH FUTURE + NOT LIVE
dfT_SGE_FN = dfT_SG[(dfT_SG['SG_Start_Date'] > todaydate) & (dfT_SG['subtitle_english'] == 'N')]

#SINGAPORE ENGLISH EXPIRING
dfT_SGE_EXP = dfT_SG[(dfT_SG['SG_Start_Date'] <= todaydate) & (dfT_SG['subtitle_english'] == 'N') & 
                   (dfT_SG['SG_End_Date'] <= mth3)]

################################################ T INDIA ################################################

#INDIA ENGLISH CURRENT + LIVE
dfT_INE_CL = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_english'] == 'Y')]

#INDIA ENGLISH FUTURE + LIVE
dfT_INE_FL = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_english'] == 'Y')]

#INDIA ENGLISH CURRENT + NOT LIVE
dfT_INE_CN = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_english'] == 'N')]

#INDIA ENGLISH FUTURE + NOT LIVE
dfT_INE_FN = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_english'] == 'N')]

#INDIA ENGLISH EXPIRING
dfT_INE_EXP = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_english'] == 'N') & 
                   (dfT_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA HINDI CURRENT + LIVE
dfT_INH_CL = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_hindi'] == 'Y')]

#INDIA HINDI FUTURE + LIVE
dfT_INH_FL = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_hindi'] == 'Y')]

#INDIA HINDI CURRENT + NOT LIVE
dfT_INH_CN = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_hindi'] == 'N')]

#INDIA HINDI FUTURE + NOT LIVE
dfT_INH_FN = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_hindi'] == 'N')]

#INDIA HINDI EXPIRING
dfT_INH_EXP = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_hindi'] == 'N') & 
                   (dfT_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TAMIL CURRENT + LIVE
dfT_INTA_CL = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_tamil'] == 'Y')]

#INDIA TAMIL FUTURE + LIVE
dfT_INTA_FL = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_tamil'] == 'Y')]

#INDIA TAMIL CURRENT + NOT LIVE
dfT_INTA_CN = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_tamil'] == 'N')]

#INDIA TAMIL FUTURE + NOT LIVE
dfT_INTA_FN = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_tamil'] == 'N')]

#INDIA TAMIL EXPIRING
dfT_INTA_EXP = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_tamil'] == 'N') & 
                   (dfT_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TELEGU CURRENT + LIVE
dfT_INTE_CL = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_telegu'] == 'Y')]

#INDIA TELEGU FUTURE + LIVE
dfT_INTE_FL = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_telegu'] == 'Y')]

#INDIA TELEGU CURRENT + NOT LIVE
dfT_INTE_CN = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_telegu'] == 'N')]

#INDIA TELEGU FUTURE + NOT LIVE
dfT_INTE_FN = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['subtitle_telegu'] == 'N')]

#INDIA TELEGU EXPIRING
dfT_INTE_EXP = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['subtitle_telegu'] == 'N') & 
                   (dfT_IN['IN_End_Date'] <= mth3)]











################################################ SD INDONESIA ################################################

#BAHASA CURRENT + LIVE
dfS_DID_CL = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['audiolanguage_bahasa'] == 'Y')]

#BAHASA FUTURE + LIVE
dfS_DID_FL = dfS_ID[(dfS_ID['ID_Start_Date'] > todaydate) & (dfS_ID['audiolanguage_bahasa'] == 'Y')]

#BAHASA CURRENT + NOT LIVE
dfS_DID_CN = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['audiolanguage_bahasa'] == 'N')]

#BAHASA FUTURE + NOT LIVE
dfS_DID_FN = dfS_ID[(dfS_ID['ID_Start_Date'] > todaydate) & (dfS_ID['audiolanguage_bahasa'] == 'N')]

#BAHASA EXPIRING
dfS_DID_EXP = dfS_ID[(dfS_ID['ID_Start_Date'] <= todaydate) & (dfS_ID['audiolanguage_bahasa'] == 'N') & 
                   (dfS_ID['ID_End_Date'] <= mth3)]

################################################ SD THAILAND ################################################

#THAI CURRENT + LIVE
dfS_DTH_CL = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['audiolanguage_thai'] == 'Y')]

#THAI FUTURE + LIVE
dfS_DTH_FL = dfS_TH[(dfS_TH['TH_Start_Date'] > todaydate) & (dfS_TH['audiolanguage_thai'] == 'Y')]

#THAI CURRENT + NOT LIVE
dfS_DTH_CN = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['audiolanguage_thai'] == 'N')]

#THAI FUTURE + NOT LIVE
dfS_DTH_FN = dfS_TH[(dfS_TH['TH_Start_Date'] > todaydate) & (dfS_TH['audiolanguage_thai'] == 'N')]

#THAI EXPIRING
dfS_DTH_EXP = dfS_TH[(dfS_TH['TH_Start_Date'] <= todaydate) & (dfS_TH['audiolanguage_thai'] == 'N') & 
                   (dfS_TH['TH_End_Date'] <= mth3)]

################################################ SD SINGAPORE ################################################

#SINGAPORE ENGLISH CURRENT + LIVE
dfS_DSGE_CL = dfS_SG[(dfS_SG['SG_Start_Date'] <= todaydate) & (dfS_SG['audiolanguage_mandarin'] == 'Y')]

#SINGAPORE ENGLISH FUTURE + LIVE
dfS_DSGE_FL = dfS_SG[(dfS_SG['SG_Start_Date'] > todaydate) & (dfS_SG['audiolanguage_mandarin'] == 'Y')]

#SINGAPORE ENGLISH CURRENT + NOT LIVE
dfS_DSGE_CN = dfS_SG[(dfS_SG['SG_Start_Date'] <= todaydate) & (dfS_SG['audiolanguage_mandarin'] == 'N')]

#SINGAPORE ENGLISH FUTURE + NOT LIVE
dfS_DSGE_FN = dfS_SG[(dfS_SG['SG_Start_Date'] > todaydate) & (dfS_SG['audiolanguage_mandarin'] == 'N')]

#SINGAPORE ENGLISH EXPIRING
dfS_DSGE_EXP = dfS_SG[(dfS_SG['SG_Start_Date'] <= todaydate) & (dfS_SG['audiolanguage_mandarin'] == 'N') & 
                   (dfS_SG['SG_End_Date'] <= mth3)]

################################################ SD INDIA ################################################

#INDIA HINDI CURRENT + LIVE
dfS_DINH_CL = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_hindi'] == 'Y')]

#INDIA HINDI FUTURE + LIVE
dfS_DINH_FL = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['audiolanguage_hindi'] == 'Y')]

#INDIA HINDI CURRENT + NOT LIVE
dfS_DINH_CN = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_hindi'] == 'N')]

#INDIA HINDI FUTURE + NOT LIVE
dfS_DINH_FN = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['audiolanguage_hindi'] == 'N')]

#INDIA HINDI EXPIRING
dfS_DINH_EXP = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_hindi'] == 'N') & 
                   (dfS_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TAMIL CURRENT + LIVE
dfS_DINTA_CL = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_tamil'] == 'Y')]

#INDIA TAMIL FUTURE + LIVE
dfS_DINTA_FL = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['audiolanguage_tamil'] == 'Y')]

#INDIA TAMIL CURRENT + NOT LIVE
dfS_DINTA_CN = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_tamil'] == 'N')]

#INDIA TAMIL FUTURE + NOT LIVE
dfS_DINTA_FN = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['audiolanguage_tamil'] == 'N')]

#INDIA TAMIL EXPIRING
dfS_DINTA_EXP = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_tamil'] == 'N') & 
                   (dfS_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TELEGU CURRENT + LIVE
dfS_DINTE_CL = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_telegu'] == 'Y')]

#INDIA TELEGU FUTURE + LIVE
dfS_DINTE_FL = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['audiolanguage_telegu'] == 'Y')]

#INDIA TELEGU CURRENT + NOT LIVE
dfS_DINTE_CN = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_telegu'] == 'N')]

#INDIA TELEGU FUTURE + NOT LIVE
dfS_DINTE_FN = dfS_IN[(dfS_IN['IN_Start_Date'] > todaydate) & (dfS_IN['audiolanguage_telegu'] == 'N')]

#INDIA TELEGU EXPIRING
dfS_DINTE_EXP = dfS_IN[(dfS_IN['IN_Start_Date'] <= todaydate) & (dfS_IN['audiolanguage_telegu'] == 'N') & 
                   (dfS_IN['IN_End_Date'] <= mth3)]






################################################ TD INDONESIA ################################################

#BAHASA CURRENT + LIVE
dfT_DID_CL = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['audiolanguage_bahasa'] == 'Y')]

#BAHASA FUTURE + LIVE
dfT_DID_FL = dfT_ID[(dfT_ID['ID_Start_Date'] > todaydate) & (dfT_ID['audiolanguage_bahasa'] == 'Y')]

#BAHASA CURRENT + NOT LIVE
dfT_DID_CN = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['audiolanguage_bahasa'] == 'N')]

#BAHASA FUTURE + NOT LIVE
dfT_DID_FN = dfT_ID[(dfT_ID['ID_Start_Date'] > todaydate) & (dfT_ID['audiolanguage_bahasa'] == 'N')]

#BAHASA EXPIRING
dfT_DID_EXP = dfT_ID[(dfT_ID['ID_Start_Date'] <= todaydate) & (dfT_ID['audiolanguage_bahasa'] == 'N') & 
                   (dfT_ID['ID_End_Date'] <= mth3)]

################################################ TD THAILAND ################################################

#THAI CURRENT + LIVE
dfT_DTH_CL = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['audiolanguage_thai'] == 'Y')]

#THAI FUTURE + LIVE
dfT_DTH_FL = dfT_TH[(dfT_TH['TH_Start_Date'] > todaydate) & (dfT_TH['audiolanguage_thai'] == 'Y')]

#THAI CURRENT + NOT LIVE
dfT_DTH_CN = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['audiolanguage_thai'] == 'N')]

#THAI FUTURE + NOT LIVE
dfT_DTH_FN = dfT_TH[(dfT_TH['TH_Start_Date'] > todaydate) & (dfT_TH['audiolanguage_thai'] == 'N')]

#THAI EXPIRING
dfT_DTH_EXP = dfT_TH[(dfT_TH['TH_Start_Date'] <= todaydate) & (dfT_TH['audiolanguage_thai'] == 'N') & 
                   (dfT_TH['TH_End_Date'] <= mth3)]

################################################ TD SINGAPORE ################################################

#SINGAPORE ENGLISH CURRENT + LIVE
dfT_DSGE_CL = dfT_SG[(dfT_SG['SG_Start_Date'] <= todaydate) & (dfT_SG['audiolanguage_mandarin'] == 'Y')]

#SINGAPORE ENGLISH FUTURE + LIVE
dfT_DSGE_FL = dfT_SG[(dfT_SG['SG_Start_Date'] > todaydate) & (dfT_SG['audiolanguage_mandarin'] == 'Y')]

#SINGAPORE ENGLISH CURRENT + NOT LIVE
dfT_DSGE_CN = dfT_SG[(dfT_SG['SG_Start_Date'] <= todaydate) & (dfT_SG['audiolanguage_mandarin'] == 'N')]

#SINGAPORE ENGLISH FUTURE + NOT LIVE
dfT_DSGE_FN = dfT_SG[(dfT_SG['SG_Start_Date'] > todaydate) & (dfT_SG['audiolanguage_mandarin'] == 'N')]

#SINGAPORE ENGLISH EXPIRING
dfT_DSGE_EXP = dfT_SG[(dfT_SG['SG_Start_Date'] <= todaydate) & (dfT_SG['audiolanguage_mandarin'] == 'N') & 
                   (dfT_SG['SG_End_Date'] <= mth3)]

################################################ TD INDIA ################################################

#INDIA HINDI CURRENT + LIVE
dfT_DINH_CL = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_hindi'] == 'Y')]

#INDIA HINDI FUTURE + LIVE
dfT_DINH_FL = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['audiolanguage_hindi'] == 'Y')]

#INDIA HINDI CURRENT + NOT LIVE
dfT_DINH_CN = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_hindi'] == 'N')]

#INDIA HINDI FUTURE + NOT LIVE
dfT_DINH_FN = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['audiolanguage_hindi'] == 'N')]

#INDIA HINDI EXPIRING
dfT_DINH_EXP = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_hindi'] == 'N') & 
                   (dfT_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TAMIL CURRENT + LIVE
dfT_DINTA_CL = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_tamil'] == 'Y')]

#INDIA TAMIL FUTURE + LIVE
dfT_DINTA_FL = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['audiolanguage_tamil'] == 'Y')]

#INDIA TAMIL CURRENT + NOT LIVE
dfT_DINTA_CN = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_tamil'] == 'N')]

#INDIA TAMIL FUTURE + NOT LIVE
dfT_DINTA_FN = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['audiolanguage_tamil'] == 'N')]

#INDIA TAMIL EXPIRING
dfT_DINTA_EXP = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_tamil'] == 'N') & 
                   (dfT_IN['IN_End_Date'] <= mth3)]

#############################################################################################################

#INDIA TELEGU CURRENT + LIVE
dfT_DINTE_CL = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_telegu'] == 'Y')]

#INDIA TELEGU FUTURE + LIVE
dfT_DINTE_FL = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['audiolanguage_telegu'] == 'Y')]

#INDIA TELEGU CURRENT + NOT LIVE
dfT_DINTE_CN = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_telegu'] == 'N')]

#INDIA TELEGU FUTURE + NOT LIVE
dfT_DINTE_FN = dfT_IN[(dfT_IN['IN_Start_Date'] > todaydate) & (dfT_IN['audiolanguage_telegu'] == 'N')]

#INDIA TELEGU EXPIRING
dfT_DINTE_EXP = dfT_IN[(dfT_IN['IN_Start_Date'] <= todaydate) & (dfT_IN['audiolanguage_telegu'] == 'N') & 
                   (dfT_IN['IN_End_Date'] <= mth3)]