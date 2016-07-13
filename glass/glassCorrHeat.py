__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

glass = pd.read_csv("glass.txt",header=None, prefix="V")

ncols = len(glass.columns)

#calculate correlation matrix for attributes only
corMat = DataFrame(glass.iloc[:,1:ncols-1].corr())
plot.pcolor(corMat)
plot.show()
