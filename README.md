# pyData :construction:

11th Feb 2019:
- [x] Added in code to clean up the dataset + create the needed dataframes
- [x] Added in import statements
- [x] Function called strip_spaces to remove white spaces
- [x] df.drop is used to remove all the uneeded columns. May need to come up with a more efficient way to do this?
- [x] Converted the existing dates in the excel to a datetime variable

11th Feb 2019 Variables:
- [x] df: to read the main excel file, and use the strip_spaces function to remove the white spaces in the listed columns
- [x] todaydate: to capture the current date (auto)
- [x] three_months: a variable to calculate what's 3 months from today's date
- [x] mth3: three_months converted to datetime
- [x] ID_Start_Date, ID_End_Date, TH_Start_Date, TH_End_Date, PH_Stat_Date, PH_End_Date, SG_Start_Date, SG_End_Date, IN_Start_Date, IN_End_Date: converted the default excel dates into datefirm format
- [x] dfS: the main dataframe for S series, derived from df
- [x] dfT: the main dataframe for T series, derived from df
- [x] dfS_ID, dfS_TH, dfS_PH, dfS_SG, dfS_IN: dataframes derived from dfS after filtering out end date
- [x] dfT_ID, dfT_TH, dfT_PH, dfT_SG, dfT_IN: dataframes derived from dfT after filtering out end date
- [x] From here, all other variables are coded based on various conditions. May need to edit for efficiency?

3rd March 2019: 
- [ ] Create a Web Server in Requests and Flask 
- [ ] Refactor Panda in TDD 
- [ ] Run Seaborn with Panda 

