import pandas as pd
from index import df

#THAILAND ENGLISH SUBS
STH_ES_CLD = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
STH_ES_FLD = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
STH_ES_CND = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
STH_ES_FND = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
STH_ES_EXP = df[(df['vod_type'] == 'SVOD') & (df['TH_Expiring'] == 'Expiring') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()

STH_ES = [STH_ES_CLD, STH_ES_FLD, STH_ES_CND, STH_ES_FND, STH_ES_EXP]

#THAILAND THAI SUBS
STH_TS_CLD = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df['TH_SUB'] == 'Live')]['duration'].sum()
STH_TS_FLD = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df['TH_SUB'] == 'Live')]['duration'].sum()
STH_TS_CND = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df['TH_SUB'] == 'Not Live')]['duration'].sum()
STH_TS_FND = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df['TH_SUB'] == 'Not Live')]['duration'].sum()
STH_TS_EXP = df[(df['vod_type'] == 'SVOD') & (df['TH_Expiring'] == 'Expiring') & (df['TH_SUB'] == 'Not Live')]['duration'].sum()

STH_TS = [STH_TS_CLD, STH_TS_FLD, STH_TS_CND, STH_TS_FND, STH_TS_EXP]

#THAILAND THAI DUBS
STH_TD_CLD = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df['TH_DUB'] == 'Live')]['duration'].sum()
STH_TD_FLD = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df['TH_DUB'] == 'Live')]['duration'].sum()
STH_TD_CND = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Current') & (df['TH_DUB'] == 'Not Live')]['duration'].sum()
STH_TD_FND = df[(df['vod_type'] == 'SVOD') & (df['TH_TimePeriod'] == 'Future') & (df['TH_DUB'] == 'Not Live')]['duration'].sum()
STH_TD_EXP = df[(df['vod_type'] == 'SVOD') & (df['TH_Expiring'] == 'Expiring') & (df['TH_DUB'] == 'Not Live')]['duration'].sum()

STH_TD = [STH_TD_CLD, STH_TD_FLD, STH_TD_CND, STH_TD_FND, STH_TD_EXP]