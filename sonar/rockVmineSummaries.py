__author__ = 'mike_bowles'
#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
with open('sonar.txt','r') as myFile:
        for line in myFile:
                row = line.strip().split(",")
                xList.append(row)

print("Number of Rows of Data = " + str(len(xList)))
print("Number of Columns of Data = " + str(len(xList[1])))
