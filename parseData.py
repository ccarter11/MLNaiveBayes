import pandas as pd 

dataframe1 = pd.read_excel("publicspreadsheet.xlsx")
print(dataframe1.head())
dataframe2 = pd.read_csv("CrimeStatistics.csv")
print(dataframe2.head())