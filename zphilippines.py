from index import dfS, dfT, todaydate, mth3
import numpy as np

#1. Filtering off expired content

dfS_PH = dfS[dfS['PH_End_Date'] >= todaydate]
dfT_PH = dfT[dfT['PH_End_Date'] >= todaydate]

#2. Creating 3 columns for S Series

dfS_PH['PH_TimePeriod'] = np.where(dfS_PH['PH_Start_Date']<=todaydate, 'Current', 'Future')
dfS_PH['PH_Expiring'] = np.where(dfS_PH['PH_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfS_PH['PH_ENG_SUB'] = np.where(dfS_PH['subtitle_english'] == 'Y', 'Live', 'Not Live')

#3. Creating 3 columns for T Series

dfT_PH['PH_TimePeriod'] = np.where(dfT_PH['PH_Start_Date']<=todaydate, 'Current', 'Future')
dfT_PH['PH_Expiring'] = np.where(dfT_PH['PH_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfT_PH['PH_ENG_SUB'] = np.where(dfT_PH['subtitle_english'] == 'Y', 'Live', 'Not Live')