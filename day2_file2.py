# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:57:29 2024

@author: Erna Leticia
"""

import pandas as pd

#df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data


url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

#df = pd.read_csv(url)
#print(df.info())
#print(df.describe())

#df = pd.read_csv("data_02/country_data_index.csv")

#df = pd.read_csv("data_02/country_data_index.csv",index_col=0)

df = pd.read_excel("data_02/residentdoctors.xlsx")

print(df.info())

"""
Regular expressions
"""

df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

print(df.info())

df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)

print(df.info())

"""
Working with dates

10-10-2024 - UK

01-10-2024 - US
"""

df = pd.read_csv("data_02/time_series_data.csv", index_col=0)

print(df.info())

# Convert the 'Date' column to datetime
#df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%Y")

df['Date'] = pd.to_datetime(df['Date'])

#df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%Y")

print(df.info())

df['Year'] = df['Date'].dt.year


# Split the 'Date' column into separate columns for year, month, and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

print(df.info())

"""
.str
.extract
.astype
"""
df = pd.read_csv("data_02/patient_data_dates.csv")

df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)

df.drop(index=26, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

print(df.info())

avg_cal = df["Calories"].mean()

df["Calories"].fillna(avg_cal, inplace = True) 

"""
best practices
"""

df.dropna(inplace = True)
df = df.reset_index(drop = True)

df.loc[7, 'Duration'] = 45


df['Duration'] = df['Duration'].replace([450], 50)

print(df)

#pd.set_option('display.max_rows',None)

################################################3

df = pd.read_csv("data_02/iris.csv")

col_names = df.columns.tolist()

print(col_names)

df["sepal_length_sq"] = df["sepal_length"]**2

df["sepal_length_sq_2"] = df["sepal_length"].apply(lambda x: x**2)

                                                   
grouped = df.groupby("class")
                                                
mean_square_values = grouped['sepal_length_sq'].mean()  

print(mean_square_values)

########################################################################

df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

df = pd.concat([df1, df2], ignore_index=True)

########################################################################

df1 = pd.read_csv('data_02/person_education.csv')
df2 = pd.read_csv('data_02/person_work.csv')

## inner join

#df_merge = pd.merge(df1,df2,on='id')

print(df)

df["class"] = df["class"].str.replace("Iris-", "")

df = df[df["sepal_length"] > 5]

df = df[df["class"] == "virginica"]

df.to_csv("output/pulsar.csv")























