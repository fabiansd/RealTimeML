import pandas as pd



import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

IMG_ROOT_PATH = os.path.join('static','plots')

def groupPlot(group,column,plot,df):
    ax=plt.figure(figsize=(12,6))
    df.groupby(group)[column].sum().sort_values().plot(plot)
    plt.ylabel(column)
    plt.xlabel(group)
    plt.show()


df = pd.read_csv('BlackFriday.csv')

# Data cleaning

df.fillna(value=0,inplace=True)
## Also looks like the product categories are float while they can be int.
df["Product_Category_2"] = df["Product_Category_2"].astype(int)
df["Product_Category_3"] = df["Product_Category_3"].astype(int)

# Replacing with named variables
df['Marital_Status'].replace(0,'Single',inplace=True)
df['Marital_Status'].replace(1,'Married',inplace=True)

# Creating new feature
df['combined_G_M'] = df.apply(lambda x:'%s_%s' % (x['Gender'],x['Marital_Status']),axis=1)

df.columns = ['User_ID', 'Product_ID', 'Kjønn', 'Alder', 'Yrke', 'By',
       'Boperiode_i_by', 'Sivilstatus', 'Produkt_kategori',
       'Product_Category_2', 'Product_Category_3', 'Salg', 'Kjønn_og_sivilstatus']

df.to_csv('BFCleaned.csv')


# Test and compare the new dataset
df_cleaned = pd.read_csv('BFCleaned.csv', index_col =0)

# print(df.info())
# print('\n')
# print(df_cleaned.info())

# groupPlot('Kjønn','Salg','bar',df)
# groupPlot('Kjønn','Salg','bar',df_cleaned)

# print('\n')
# print(df.head(10))
# print('\n')
# print(df_cleaned.head(10))
# print('\n')