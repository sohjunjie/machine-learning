__author__ = 'mike-bowles'
import numpy
from sklearn import datasets, linear_model
from math import sqrt
import matplotlib.pyplot as plot

xList = []
labels = []
names = []
firstLine = True
with open('winequality-red.csv','r') as myFile:
    for line in myFile:
        if firstLine:
            names = line.strip().split(";")
            firstLine = False
        else:
            row = line.strip().split(";")
            labels.append(float(row[-1]))
            row.pop()
            floatRow = [float(num) for num in row]
            xList.append(floatRow)
