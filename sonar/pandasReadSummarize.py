__author__ = 'mike_bowles'
import pandas as pd

rocksVMines = pd.read_csv("sonar.txt",header=None, prefix="V")

print(rocksVMines.head())
print(rocksVMines.tail())

#print summary of data frame
summary = rocksVMines.describe()
print(summary)
