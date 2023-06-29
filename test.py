import pandas as pd
from pandasgui import show
df = pd.read_csv('cars.csv')

print(df.columns)


df2 = df.groupby('engine_type').count()

#df2 = df.plot(x='model_name', y='price_usd', kind='line')

show(df2)