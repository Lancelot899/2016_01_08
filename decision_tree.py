#!/usr/bin/python
#coding = utf-8

import information_entropy

def spliteDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet



def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = information_entropy.calcEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in xrange(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = spliteDataSet(dataSet, i, value)
            prob = len(subDataSet)/ float(len(dataSet))
            newEntropy += prob * information_entropy.calcEntropy(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

import operator

def majorityCnt(classList):
    classCnt = {}
    for vote in classList:
        classCnt[vote] =  classCnt.get(vote, 0) + 1
    sortedClassCnt = sorted(classCnt.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCnt[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(spliteDataSet(dataSet,bestFeat,value), subLabels)
    return myTree

if __name__ == '__main__':
    dataSet = [[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'],[1,1,'yes']]
    labels = ['one', 'two', 'answer']
    tree = createTree(dataSet, labels)
    print tree
