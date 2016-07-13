__author__ = 'mike_bowles'
#arrange data into list for labels and list of lists for attributes
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

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0] * 3

print("Col#" + '\t' + "Number" + '\t' + "Strings" + '\t' + "Other")

iCol = 0
for types in colCounts:
    print(str(iCol) + '\t' + str(types[0]) + '\t' + str(types[1]) + '\t' + str(types[2]))
    iCol += 1
