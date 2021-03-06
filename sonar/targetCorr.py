__author__ = 'mike_bowles'
import pandas as pd
import matplotlib.pyplot as plot
from random import uniform

rocksVMines = pd.read_csv("sonar.txt",header=None, prefix="V")

#change the targets to numeric values
target = []
for i in range(208):
    #assign 0 or 1 target value based on "M" or "R" labels
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

#plot 35th attribute
dataRow = rocksVMines.iloc[0:208,35]

plot.scatter(dataRow, target)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

#To improve the visualization, this version dithers the points a little
# and makes them somewhat transparent
target = []
for i in range(208):
#assign 0 or 1 target value based on "M" or "R" labels and add some dither
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))

#plot 35th attribute with semi-opaque points
dataRow = rocksVMines.iloc[0:208,35]

plot.scatter(dataRow, target, alpha=0.5, s=120)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()
