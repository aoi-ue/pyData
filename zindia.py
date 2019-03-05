from index import dfS, dfT, todaydate, mth3
import numpy as np

#1. Filtering off expired content

dfS_IN = dfS[dfS['IN_End_Date'] >= todaydate]
dfT_IN = dfT[dfT['IN_End_Date'] >= todaydate]

#2. Creating 9 columns for S Series

dfS_IN['IN_TimePeriod'] = np.where(dfS_IN['IN_Start_Date']<=todaydate, 'Current', 'Future')
dfS_IN['IN_Expiring'] = np.where(dfS_IN['IN_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfS_IN['IN_ENG_SUB'] = np.where(dfS_IN['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfS_IN['IN_HIN_SUB'] = np.where(dfS_IN['subtitle_hindi'] == 'Y', 'Live', 'Not Live')
dfS_IN['IN_TAM_SUB'] = np.where(dfS_IN['subtitle_tamil'] == 'Y', 'Live', 'Not Live')
dfS_IN['IN_TEL_SUB'] = np.where(dfS_IN['subtitle_telegu'] == 'Y', 'Live', 'Not Live')
dfS_IN['IN_HIN_DUB'] = np.where(dfS_IN['audiolanguage_hindi'] == 'Y', 'Live', 'Not Live')
dfS_IN['IN_TAM_DUB'] = np.where(dfS_IN['audiolanguage_tamil'] == 'Y', 'Live', 'Not Live')
dfS_IN['IN_TEL_DUB'] = np.where(dfS_IN['audiolanguage_telegu'] == 'Y', 'Live', 'Not Live')

#3. Creating 9 columns for T Series

dfT_IN['IN_TimePeriod'] = np.where(dfT_IN['IN_Start_Date']<=todaydate, 'Current', 'Future')
dfT_IN['IN_Expiring'] = np.where(dfT_IN['IN_End_Date'] <= mth3, 'Expiring', 'Not Expiring')
dfT_IN['IN_ENG_SUB'] = np.where(dfT_IN['subtitle_english'] == 'Y', 'Live', 'Not Live')
dfT_IN['IN_HIN_SUB'] = np.where(dfT_IN['subtitle_hindi'] == 'Y', 'Live', 'Not Live')
dfT_IN['IN_TAM_SUB'] = np.where(dfT_IN['subtitle_tamil'] == 'Y', 'Live', 'Not Live')
dfT_IN['IN_TEL_SUB'] = np.where(dfT_IN['subtitle_telegu'] == 'Y', 'Live', 'Not Live')
dfT_IN['IN_HIN_DUB'] = np.where(dfT_IN['audiolanguage_hindi'] == 'Y', 'Live', 'Not Live')
dfT_IN['IN_TAM_DUB'] = np.where(dfT_IN['audiolanguage_tamil'] == 'Y', 'Live', 'Not Live')
dfT_IN['IN_TEL_DUB'] = np.where(dfT_IN['audiolanguage_telegu'] == 'Y', 'Live', 'Not Live')