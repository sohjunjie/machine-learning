__author__ = 'mike_bowles'
#arrange data into list for labels and list of lists for attributes
import numpy as np

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

#generate summary statistics for column 3
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)

print("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t ' + str(colsd))

#calculate quantile boundaries
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

print("\nBoundaries for 4 Equal Percentiles")
print(percentBdry)

#calculate quantile boundaries with 10 interval
ntiles = 10
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

print("\nBoundaries for 10 Equal Percentiles")
print(percentBdry)

#The last column contains categorical variables
col = 60
colData = []
for row in xList:
    colData.append(row[col])

unique = set(colData)
print("Unique Label Values")
print(unique)

#count up the number of elements having each value
catDict = dict(zip(list(unique),range(len(unique))))
catCount = [0]*2
for elt in colData:
    catCount[catDict[elt]] += 1

print("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)
