from index import dfS, dfT, todaydate, mth3
import numpy as np

#1. Filtering off expired content

dfS_ID = dfS[dfS['ID_End_Date'] >= todaydate]
dfT_ID = dfT[dfT['ID_End_Date'] >= todaydate]

#2. Creating 5 columns for S Series

dfS_ID['ID_TimePeriod'] = np.where(dfS_ID['ID_Start_Date']<=todaydate, 'Current', 'Future')
dfS_ID['ID_Expiring'] = np.where(dfS_ID['ID_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfS_ID['ID_BH_SUB'] = np.where(dfS_ID['subtitle_bahasa'] == 'Y', 'Live', 'Not Live')
dfS_ID['ID_ENG_SUB'] = np.where(dfS_ID['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfS_ID['ID_BH_DUB'] = np.where(dfS_ID['audiolanguage_bahasa'] == 'Y', 'Live', 'Not Live')

#3. Creating 5 columns for T Series

dfT_ID['ID_TimePeriod'] = np.where(dfT_ID['ID_Start_Date']<=todaydate, 'Current', 'Future')
dfT_ID['ID_Expiring'] = np.where(dfT_ID['ID_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfT_ID['ID_BH_SUB'] = np.where(dfT_ID['subtitle_bahasa'] == 'Y', 'Live', 'Not Live')
dfT_ID['ID_ENG_SUB'] = np.where(dfT_ID['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfT_ID['ID_BH_DUB'] = np.where(dfT_ID['audiolanguage_bahasa'] == 'Y', 'Live', 'Not Live')