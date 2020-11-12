import numpy as np
import pandas as pd

def testdDfDate(dfStudent):
    
    df = pd.read_csv('IthacaDailyClimate2018.csv', parse_dates=['Date'])
    if not isinstance(dfStudent, pd.DataFrame):
        return "Incorrect!\nMake sure you are reading in the correct file."
    if not df.equals(dfStudent):
        return "Incorrect!\nMake sure you reading in the correct file and using the parse_dates option to parse the Data column as dates."
    if not pd.core.dtypes.common.is_datetime_or_timedelta_dtype(dfStudent['Date']):
        return "Incorrect!\nMake sure you are using the parse_dates option to parse the Data column as dates."
    return "Correct!"

def testSnow16(snow16, dfStudent):
    
    df16 = pd.read_excel('IthacaDailyClimateMultiyear.xlsx', sheet_name='2016')
    if not df16.equals(dfStudent):
        return "Incorrect!\nMake sure you read in the correct file and sheet name and assigned the dataframe to df16."
    if not snow16 == df16['Snowfall'].sum():
        return "Incorrect!\nsnow16 does not contain the total amount of Snowfall in Ithaca during 2016.\n"
    return "Correct!\nsnow16 contains the total amount of Snowfall in Ithaca during 2016."
    
def testSnow18(snow18, dfStudent):
 
    df18 = pd.read_excel('IthacaDailyClimateMultiyear.xlsx', sheet_name='2018')
    if not df18.equals(dfStudent):
        return "Incorrect!\nMake sure you read in the correct file and sheet name and assigned the dataframe to df18."
    if not snow18 == df18['Snowfall'].sum():
        return "Incorrect!\nsnow16 does not contain the total amount of Snowfall in Ithaca during 2018.\n"
    return "Correct!\nsnow18 contains the total amount of Snowfall in Ithaca during 2018."

def testMoreSnow(year):
    
    if isinstance(year, int):
        year = str(year)
        
    if not year == '2018':
        return "Incorrect!"
    
    return "Correct!"
    
