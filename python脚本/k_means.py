# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:02:20 2019

@author: HASEE
"""

import numpy as np
import random
import re
import matplotlib.pyplot as plt

def show_fig():
    dataSet = loadDataSet()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataSet[:, 0], dataSet[:, 1])
    plt.show()

def calcuDistance(vec1, vec2):# Calculate the Euclidean distance between vectors 1 and 2
    return np.sqrt(np.sum(np.square(vec1 - vec2)))  

def loadDataSet():
    dataSet = np.loadtxt("train_data.txt")
    return dataSet

def initCentroids(dataSet, k):    # random select k as dataset-sample
    dataSet = list(dataSet)
    return random.sample(dataSet, k)

def minDistance(dataSet, centroidList):#to cal the min_distance 
    clusterDict = dict() #save the result
    k = len(centroidList)
    for item in dataSet:
        vec1 = item
        flag = -1
        minDis = float("inf") # initial the inf
        for i in range(k):
            vec2 = centroidList[i]
            distance = calcuDistance(vec1, vec2)  # error
            if distance < minDis:
                minDis = distance
                flag = i  
        if flag not in clusterDict.keys():
            clusterDict.setdefault(flag, [])
        clusterDict[flag].append(item)  
    return clusterDict  

def getCentroids(clusterDict): #Recalculate k centroids
    centroidList = []
    for key in clusterDict.keys():
        centroid = np.mean(clusterDict[key], axis=0)
        centroidList.append(centroid)
    return centroidList  #get new centroids


def getVar(centroidList, clusterDict):#cal the mean error and sum the vector in the class
    sum = 0.0
    for key in clusterDict.keys():
        vec1 = centroidList[key]
        distance = 0.0
        for item in clusterDict[key]:
            vec2 = item
            distance += calcuDistance(vec1, vec2)
        sum += distance
    return sum

def showCluster(centroidList, clusterDict):#show the result
    colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow'] 
    centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']

    for key in clusterDict.keys():
        plt.plot(centroidList[key][0], centroidList[key][1], centroidMark[key], markersize=12) #质心点
        for item in clusterDict[key]:
            plt.plot(item[0], item[1], colorMark[key])
    plt.show()


def test_k_means():
    dataSet = loadDataSet()
    centroidList = initCentroids(dataSet, 4)
    clusterDict = minDistance(dataSet, centroidList)
    # # getCentroids(clusterDict)
    # showCluster(centroidList, clusterDict)
    newVar = getVar(centroidList, clusterDict)
    oldVar = 1  

    times = 2
    while abs(newVar - oldVar) >= 0.00001:
        centroidList = getCentroids(clusterDict)
        clusterDict = minDistance(dataSet, centroidList)
        oldVar = newVar
        newVar = getVar(centroidList, clusterDict)
        times += 1
        showCluster(centroidList, clusterDict)

if __name__ == '__main__':
    # show_fig()
    test_k_means()


