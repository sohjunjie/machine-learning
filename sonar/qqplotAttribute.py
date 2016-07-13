__author__ = 'mike_bowles'
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

xList = []
labels = []
with open('sonar.txt','r') as myFile:
    for line in myFile:
        row = line.strip().split(",")
        xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0] * 3
colCounts = []

#generate summary statistics for column 3 (e.g.)
col = 3
colData = []

for row in xList:
    colData.append(float(row[col]))

stats.probplot(colData, dist="norm", plot=plt)
plt.show()
