import pandas as pd

dfc = pd.read_csv('IthacaDailyClimate2018.csv')

minvals = dfc.min()
print(minvals)

dfc.info()

meanvals = dfc.mean()
print(meanvals)

sumvals = dfc.sum()
print(sumvals)

dfcdesc = dfc.describe()
