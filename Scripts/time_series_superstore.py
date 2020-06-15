import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path = "E:/MyWorkStation/MM Work/Datasets/Superstore.xls"
import datetime as dt
df = pd.read_excel(path,usecols=['Order Date','Category','Sales'])

furniture = df[df.Category == 'Furniture'].set_index('Order Date')
furniture.drop('Category',inplace=True,axis=1)
furniture_resample = furniture.resample('M').mean()

plt.style.use('dark_background')
furniture_resample.plot(figsize=(14,6))