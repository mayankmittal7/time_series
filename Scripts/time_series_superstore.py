import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path = "E:/MyWorkStation/MM Work/Datasets/Superstore.xls"
import datetime as dt
df = pd.read_excel(path,usecols=[''])

for values in df.Category.value_counts().index:
    values = df[df.Category == values]