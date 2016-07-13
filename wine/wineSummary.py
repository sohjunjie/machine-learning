__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

wine = pd.read_csv("winequality-red.csv",header=0, sep=";")
print(wine.head())

#generate statistical summaries
summary = wine.describe()
print(summary)

wineNormalized = wine
ncols = len(wineNormalized.columns)

for i in range(ncols):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    wineNormalized.iloc[:,i:(i + 1)] = (wineNormalized.iloc[:,i:(i + 1)] - mean) / sd

array = wineNormalized.values
plot.boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges - Normalized ")
plot.show()
