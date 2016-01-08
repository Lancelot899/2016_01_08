#!/usr/bin/python
#coding = utf-8

import decision_tree
import plotTree

dataSet = [[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'],[1,1,'yes']]
labels = ['one', 'two', 'answer']

tree = decision_tree.createTree(dataSet, labels)
plotTree.createPlot()
