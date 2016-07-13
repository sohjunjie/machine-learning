__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

abalone = pd.read_csv("abalone.txt",header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height',
                    'Whole weight','Shucked weight', 'Viscera weight',
                    'Shell weight', 'Rings']

print(abalone.head())
print(abalone.tail())

#print summary of data frame
summary = abalone.describe()
print(summary)

array = abalone.iloc[:,1:9].values
plot.boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
plot.show()

#the last column (rings) is out of scale with the rest
# - remove and replot
array2 = abalone.iloc[:,1:8].values
plot.boxplot(array2)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
plot.show()


abaloneNormalized = abalone.iloc[:,1:9]

for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    abaloneNormalized.iloc[:,i:(i + 1)] = (abaloneNormalized.iloc[:,i:(i + 1)] - mean) / sd


array3 = abaloneNormalized.values
plot.boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized "))
plot.show()
