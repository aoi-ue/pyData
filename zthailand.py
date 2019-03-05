from index import dfS, dfT, todaydate, mth3
import numpy as np

#1. Filtering off expired content

dfS_TH = dfS[dfS['TH_End_Date'] >= todaydate]
dfT_TH = dfT[dfT['TH_End_Date'] >= todaydate]

#2. Creating 5 columns for S Series

dfS_TH['TH_TimePeriod'] = np.where(dfS_TH['TH_Start_Date']<=todaydate, 'Current', 'Future')
dfS_TH['TH_Expiring'] = np.where(dfS_TH['TH_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfS_TH['TH_TH_SUB'] = np.where(dfS_TH['subtitle_thai'] == 'Y', 'Live', 'Not Live')
dfS_TH['TH_ENG_SUB'] = np.where(dfS_TH['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfS_TH['TH_TH_DUB'] = np.where(dfS_TH['audiolanguage_thai'] == 'Y', 'Live', 'Not Live')

#3. Creating 5 columns for S Series

dfT_TH['TH_TimePeriod'] = np.where(dfT_TH['TH_Start_Date']<=todaydate, 'Current', 'Future')
dfT_TH['TH_Expiring'] = np.where(dfT_TH['TH_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfT_TH['TH_TH_SUB'] = np.where(dfT_TH['subtitle_thai'] == 'Y', 'Live', 'Not Live')
dfT_TH['TH_ENG_SUB'] = np.where(dfT_TH['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfT_TH['TH_TH_DUB'] = np.where(dfT_TH['audiolanguage_thai'] == 'Y', 'Live', 'Not Live')