import xlrd
import pandas as pd

xlsfile = pd.ExcelFile('E:\\Python Projects\\pyData\\DataDump\\SINGTEL_INGESTION_EXTRACT_2018-12-26.xlsx')
dframe = xlsfile.parse('Sheet1')

print(dframe['lic_start_date_india'])