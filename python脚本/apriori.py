# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:52:01 2019

@author: HASEE
"""
def get_data():#to load the data from the data file
    all_usr=[]
    usr=[]
    usr_case=""
    with open("anonymous-msweb.data",mode="r") as f:
        for i in f:
            if "C" in i:
                if len(usr)!=0:
                    usr_case=usr_case.rstrip(",")
                    usr.append(usr_case)
                    all_usr.append(usr)
                    usr=[]
                    usr_case=""
                #i=i.strip("\n")
                usr.append(i[10:15])
                continue
            else:
                usr_case+=(i[2:6]+",")
    return all_usr# return all the usr click num

def data_preprocess(all_usr):#to clean the data for analysis
    dataSet=[]
    for i in range(len(all_usr)):
        dataSet.append(all_usr[i][1])
    for i in range(len(dataSet)):
        dataSet[i]=dataSet[i].split(",")
    return dataSet


def createC1(dataSet):#create the 1-item dataset 
    C1 = set()
    for transaction in dataSet:
        for item in transaction:
            C1.add(item)
    C1 = list(C1)
    C1.sort()
    return map(lambda x:frozenset([x]), C1)#use frozenset to convenient use of key

def scanD(D, Ck, minSupport):#ck represent the  candidate dataset consists of k_num item 
    ssCnt = {}
    D=list(D)
    Ck=list(Ck)
    for tid in D:#D represent the whole dataset 
        for can in Ck:#Ck candidate set
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1
                #print("1")
    #print(ssCnt)
    numItems = float(len(D))
    retList = []
    supportData = {}#to cal  the support of every item in Ck
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)#filtering
        supportData[key] = support
        #print("2")
    return retList, supportData#retList represent the element that greater than min_support
def aprioriGen(Lk, k):#depending on aftering (filtering Lk) to create candidate set Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList
def apriori(dataSet, minSupport=0.5):#to call other functions and set up the min_support 
    C1 = list(createC1(dataSet))
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    #to estimate the candidate dataset
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print (freqSet - conseq, '-->', conseq, 'conf:', conf)
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    # to create the rule 
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmpl = aprioriGen(H, m + 1)
        Hmpl = calcConf(freqSet, Hmpl, supportData, brl, minConf)
        if (len(Hmpl) > 1):
            rulesFromConseq(freqSet, Hmpl, supportData, brl, minConf)
def generateRules(L, supportData, minConf=0.7):#set up the min_confidence to generate the rule 
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                # dataset that more than three elment
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                #cal confidence
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList
dataSet=data_preprocess(get_data())
L,suppDat=apriori(dataSet,0.01)
rule=generateRules(L,suppDat,0.8)
#print(rule)