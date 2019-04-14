import pandas as pd
from index import df

#SINGAPORE ENGLISH SUBS
SSG_ES_CLD = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SSG_ES_FLD = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Live')]['duration'].sum()
SSG_ES_CND = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Current') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SSG_ES_FND = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Future') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()
SSG_ES_EXP = df[(df['vod_type'] == 'SVOD') & (df['SG_Expiring'] == 'Expiring') & (df['ENG_SUB'] == 'Not Live')]['duration'].sum()

SSG_ES = [SSG_ES_CLD, SSG_ES_FLD, SSG_ES_CND, SSG_ES_FND, SSG_ES_EXP]

#SINGAPORE MANDARIN DUBS
SSG_MD_CLD = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Current') & (df['MAN_DUB'] == 'Live')]['duration'].sum()
SSG_MD_FLD = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Future') & (df['MAN_DUB'] == 'Live')]['duration'].sum()
SSG_MD_CND = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Current') & (df['MAN_DUB'] == 'Not Live')]['duration'].sum()
SSG_MD_FND = df[(df['vod_type'] == 'SVOD') & (df['SG_TimePeriod'] == 'Future') & (df['MAN_DUB'] == 'Not Live')]['duration'].sum()
SSG_MD_EXP = df[(df['vod_type'] == 'SVOD') & (df['SG_Expiring'] == 'Expiring') & (df['MAN_DUB'] == 'Not Live')]['duration'].sum()

SSG_MD = [SSG_MD_CLD, SSG_MD_FLD, SSG_MD_CND, SSG_MD_FND, SSG_MD_EXP]

