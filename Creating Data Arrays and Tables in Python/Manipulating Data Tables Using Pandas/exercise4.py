import pandas as pd

dfp = pd.read_excel('PizzaSheet.xlsx')

print(dfp.shape)

dfp.info()
print(dfp.info)

dfc = pd.read_csv('IthacaDailyClimate2018.csv')
