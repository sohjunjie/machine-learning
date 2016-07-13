__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

abalone = pd.read_csv("abalone.txt",header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height',
                    'Whole weight','Shucked weight', 'Viscera weight',
                    'Shell weight', 'Rings']

#calculate correlation matrix
corMat = DataFrame(abalone.iloc[:,1:9].corr())
print(corMat)

#visualize correlations using heatmap
plot.pcolor(corMat)
plot.show()
