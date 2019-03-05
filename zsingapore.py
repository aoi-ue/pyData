from index import dfS, dfT, todaydate, mth3
import numpy as np

#1. Filtering off expired content

dfS_SG = dfS[dfS['SG_End_Date'] >= todaydate]
dfT_SG = dfT[dfT['SG_End_Date'] >= todaydate]

#2. Creating 4 columns for S Series

dfS_SG['SG_TimePeriod'] = np.where(dfS_SG['SG_Start_Date']<=todaydate, 'Current', 'Future')
dfS_SG['SG_Expiring'] = np.where(dfS_SG['SG_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfS_SG['SG_ENG_SUB'] = np.where(dfS_SG['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfS_SG['SG_MAN_DUB'] = np.where(dfS_SG['audiolanguage_mandarin'] == 'Y', 'Live', 'Not Live')

#3. Creating 4 columns for T Series

dfT_SG['SG_TimePeriod'] = np.where(dfT_SG['SG_Start_Date']<=todaydate, 'Current', 'Future')
dfT_SG['SG_Expiring'] = np.where(dfT_SG['SG_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfT_SG['SG_ENG_SUB'] = np.where(dfT_SG['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfT_SG['SG_MAN_DUB'] = np.where(dfT_SG['audiolanguage_mandarin'] == 'Y', 'Live', 'Not Live')