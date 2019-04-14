import pandas as pd
from index import df

#INDONESIA SVOD ENG_SUB
SID_ES_CLD = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SID_ES_FLD = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SID_ES_CND = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SID_ES_FND = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SID_ES_EXP = df[(df['vod_type'] == 'SVOD') & (df['ID_Expiring'] == 'Expiring') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()

SID_ES = [SID_ES_CLD, SID_ES_FLD, SID_ES_CND, SID_ES_FND, SID_ES_EXP]

#INDONESIA SVOD BH_SUB
SID_BS_CLD = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df['BH_SUB'] == 'Live')]['duration'].sum()
SID_BS_FLD = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df['BH_SUB'] == 'Live')]['duration'].sum()
SID_BS_CND = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df['BH_SUB'] == 'Not Live')]['duration'].sum()
SID_BS_FND = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df['BH_SUB'] == 'Not Live')]['duration'].sum()
SID_BS_EXP = df[(df['vod_type'] == 'SVOD') & (df['ID_Expiring'] == 'Expiring') & (df['BH_SUB'] == 'Not Live')]['duration'].sum()

SID_BS = [SID_BS_CLD, SID_BS_FLD, SID_BS_CND, SID_BS_FND, SID_BS_EXP]

#INDONESIA SVOD BH_DUB
SID_BD_CLD = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df['BH_DUB'] == 'Live')]['duration'].sum()
SID_BD_FLD = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df['BH_DUB'] == 'Live')]['duration'].sum()
SID_BD_CND = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Current') & (df['BH_DUB'] == 'Not Live')]['duration'].sum()
SID_BD_FND = df[(df['vod_type'] == 'SVOD') & (df['ID_TimePeriod'] == 'Future') & (df['BH_DUB'] == 'Not Live')]['duration'].sum()
SID_BD_EXP = df[(df['vod_type'] == 'SVOD') & (df['ID_Expiring'] == 'Expiring') & (df['BH_DUB'] == 'Not Live')]['duration'].sum()

SID_BD = [SID_BD_CLD, SID_BD_FLD, SID_BD_CND, SID_BD_FND, SID_BD_EXP]