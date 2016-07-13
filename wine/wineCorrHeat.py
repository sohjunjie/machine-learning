__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

wine = pd.read_csv("winequality-red.csv",header=0, sep=";")

ncols = len(wine.columns)

#calculate correlation matrix
corMat = DataFrame(wine.iloc[:,:ncols].corr())
plot.pcolor(corMat)
plot.show()
