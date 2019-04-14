import pandas as pd
from index import df

#INDIA ENGLISH SUBS
SIN_ES_CLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SIN_ES_FLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SIN_ES_CND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SIN_ES_FND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SIN_ES_EXP = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()

SIN_ES = [SIN_ES_CLD, SIN_ES_FLD, SIN_ES_CND, SIN_ES_FND, SIN_ES_EXP]

#INDIA HINDI SUBS
SIN_HS_CLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['HIN_SUB'] == 'Live')]['duration'].sum()
SIN_HS_FLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['HIN_SUB'] == 'Live')]['duration'].sum()
SIN_HS_CND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['HIN_SUB'] == 'Not Live')]['duration'].sum()
SIN_HS_FND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['HIN_SUB'] == 'Not Live')]['duration'].sum()
SIN_HS_EXP = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df['HIN_SUB'] == 'Not Live')]['duration'].sum()

SIN_HS = [SIN_HS_CLD, SIN_HS_FLD, SIN_HS_CND, SIN_HS_FND, SIN_HS_EXP]

#INDIA TAMIL SUBS
SIN_TS_CLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TAM_SUB'] == 'Live')]['duration'].sum()
SIN_TS_FLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TAM_SUB'] == 'Live')]['duration'].sum()
SIN_TS_CND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TAM_SUB'] == 'Not Live')]['duration'].sum()
SIN_TS_FND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TAM_SUB'] == 'Not Live')]['duration'].sum()
SIN_TS_EXP = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df['TAM_SUB'] == 'Not Live')]['duration'].sum()

SIN_TS = [SIN_TS_CLD, SIN_TS_FLD, SIN_TS_CND, SIN_TS_FND, SIN_TS_EXP]

#INDIA TELEGU SUBS
SIN_TES_CLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TEL_SUB'] == 'Live')]['duration'].sum()
SIN_TES_FLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TEL_SUB'] == 'Live')]['duration'].sum()
SIN_TES_CND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TEL_SUB'] == 'Not Live')]['duration'].sum()
SIN_TES_FND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TEL_SUB'] == 'Not Live')]['duration'].sum()
SIN_TES_EXP = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df['TEL_SUB'] == 'Not Live')]['duration'].sum()

SIN_TES = [SIN_TES_CLD, SIN_TES_FLD, SIN_TES_CND, SIN_TES_FND, SIN_TES_EXP]

#INDIA HINDI DUBS
SIN_HD_CLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['HIN_DUB'] == 'Live')]['duration'].sum()
SIN_HD_FLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['HIN_DUB'] == 'Live')]['duration'].sum()
SIN_HD_CND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['HIN_DUB'] == 'Not Live')]['duration'].sum()
SIN_HD_FND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['HIN_DUB'] == 'Not Live')]['duration'].sum()
SIN_HD_EXP = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df['HIN_DUB'] == 'Not Live')]['duration'].sum()

SIN_HD = [SIN_HD_CLD, SIN_HD_FLD, SIN_HD_CND, SIN_HD_FND, SIN_HD_EXP]

#INDIA TAMIL DUBS
SIN_TD_CLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TAM_DUB'] == 'Live')]['duration'].sum()
SIN_TD_FLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TAM_DUB'] == 'Live')]['duration'].sum()
SIN_TD_CND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TAM_DUB'] == 'Not Live')]['duration'].sum()
SIN_TD_FND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TAM_DUB'] == 'Not Live')]['duration'].sum()
SIN_TD_EXP = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df['TAM_DUB'] == 'Not Live')]['duration'].sum()

SIN_TD = [SIN_TD_CLD, SIN_TD_FLD, SIN_TD_CND, SIN_TD_FND, SIN_TD_EXP]

#INDIA TELEGU DUBS
SIN_TED_CLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TEL_DUB'] == 'Live')]['duration'].sum()
SIN_TED_FLD = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TEL_DUB'] == 'Live')]['duration'].sum()
SIN_TED_CND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Current') & (df['TEL_DUB'] == 'Not Live')]['duration'].sum()
SIN_TED_FND = df[(df['vod_type'] == 'SVOD') & (df['IN_TimePeriod'] == 'Future') & (df['TEL_DUB'] == 'Not Live')]['duration'].sum()
SIN_TED_EXP = df[(df['vod_type'] == 'SVOD') & (df['IN_Expiring'] == 'Expiring') & (df['TEL_DUB'] == 'Not Live')]['duration'].sum()

SIN_TED = [SIN_TED_CLD, SIN_TED_FLD, SIN_TED_CND, SIN_TED_FND, SIN_TED_EXP]