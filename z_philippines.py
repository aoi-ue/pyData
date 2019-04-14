import pandas as pd
from index import df

#PHILIPPINES ENGLISH SUBS
SPH_ES_CLD = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SPH_ES_FLD = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SPH_ES_CND = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SPH_ES_FND = df[(df['vod_type'] == 'SVOD') & (df['PH_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SPH_ES_EXP = df[(df['vod_type'] == 'SVOD') & (df['PH_Expiring'] == 'Expiring') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()

SPH_ES = [SPH_ES_CLD, SPH_ES_FLD, SPH_ES_CND, SPH_ES_FND, SPH_ES_EXP]