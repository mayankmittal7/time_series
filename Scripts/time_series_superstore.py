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

Office_Supplies = df[df.Category == 'Office Supplies'].set_index('Order Date')
Office_Supplies.drop('Category',inplace=True,axis=1)
Office_Supplies_resample = Office_Supplies.resample('M').mean()

Technology = df[df.Category == 'Technology'].set_index('Order Date')
Technology.drop('Category',inplace=True,axis=1)
Technology_resample = Technology.resample('M').mean()

plt.plot(furniture_resample,'b-',label='furniture')
plt.plot(Office_Supplies_resample,'r-',label='office')
plt.plot(Technology_resample,'g-',label='technology')
plt.xlabel('Dates')
plt.ylabel('Category')
plt.title('Sales of different Categories')
plt.legend()

