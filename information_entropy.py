#!/usr/bin/python
#coding = utf-8

from math import log

def calcEntropy(dataSet):
    numEntries = len(dataSet)
    labelCnts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        labelCnts[currentLabel] = labelCnts.get(currentLabel, 0) + 1
    Entropy = 0.0
    for key in labelCnts:
        prob = float(labelCnts[key]) / numEntries
        Entropy -= prob * log(prob, 2)
    return Entropy

if __name__ == '__main__':
    dataSet = [[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'],[1,1,'yes']]
    print calcEntropy(dataSet)
