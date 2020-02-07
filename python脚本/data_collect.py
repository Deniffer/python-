import os
import pandas as pd
import re
path=r"D:\qqdownload\sampledata2\sampledata2"# 这个要修改成本地你放csv文件的路径
os.chdir(path)
file=os.listdir(path)
#print(file)
all_csv=[i for i in file if ".csv" in i]
#print(all_csv)
name=[]
ID=[]
name_1=[]
for i in all_csv:
    name.extend(re.findall(r"cost(.+?)_Behavior",i))
for i in name:
    ID.extend(re.findall(r"\d{4}",i))
    name_1.append(i[8:])
def avg_exposure(df):
    left_avg_exposure=[]
    right_avg_exposure=[]
    up_avg_exposure=[]
    left_avg=0
    right_avg=0
    up_avg=0
    for i in range(len(df)):
        if df["Response"].values[i]=="right":
            right_avg_exposure.append(df["Exposure_time"].values[i])
        elif df["Response"].values[i]=="left":
            left_avg_exposure.append(df["Exposure_time"].values[i])
        else:
            up_avg_exposure.append(df["Exposure_time"].values[i])
    try:
        left_avg=sum(left_avg_exposure)/len(left_avg_exposure)
    except:
        left_avg=0
    try:    
        right_avg=sum(right_avg_exposure)/len(right_avg_exposure)
    except:
        right_avg=0
    if len(up_avg_exposure)!=0:
        up_avg=sum(up_avg_exposure)/len(up_avg_exposure)
    return left_avg,right_avg,up_avg

def avg_of_exposure_and_rt(df):
    left_avg_exposure=[]
    right_avg_exposure=[]
    up_avg_exposure=[]
    left_avg=0
    right_avg=0
    up_avg=0
    for i in range(len(df)):
        if df["Response"].values[i]=="right":
            right_avg_exposure.append(df["Exposure_time"].values[i]+df["RT"].values[i])
        elif df["Response"].values[i]=="left":
            left_avg_exposure.append(df["Exposure_time"].values[i]+df["RT"].values[i])
        else:
            up_avg_exposure.append(df["Exposure_time"].values[i]+df["RT"].values[i])
    left_avg=sum(left_avg_exposure)/len(left_avg_exposure)
    right_avg=sum(right_avg_exposure)/len(right_avg_exposure)
    if len(up_avg_exposure)!=0:
        up_avg=sum(up_avg_exposure)/len(up_avg_exposure)
    return left_avg,right_avg,up_avg

def get_count(df):
    total=df["Response"].value_counts()
    right=total['right']
    left=total['left']
    try:
        up=0
        up=df["Response"].value_counts()['up']
    except:
        pass 
    return left,right,up
def get_exposure_csv():
    df_2=pd.DataFrame(columns=pd.MultiIndex.from_product([['5_option2','15_option2','5_option3','15_option3'],['left','right','up']]),index=set(ID))
    for i in range(len(all_csv)):
        option=['15_option2','15_option3','5_option3','5_option2']
        df=pd.read_csv(all_csv[i],encoding="latin1")
        left,right,up=avg_exposure(df)
        for j in set(ID):#csv_id is record the id 
            if j in name[i]:
                csv_id=j
                #break
        for j in option:
            if j == name_1[i]:
                csv_column=j
                #break
        df_2[csv_column,"left"][csv_id]=left
        df_2[csv_column,"right"][csv_id]=right
        df_2[csv_column,"up"][csv_id]=up
    df_2=df_2.fillna(0)
    df_2.to_csv("exposure_avg.csv",encoding="latin1")
get_exposure_csv()

def get_exposure_add_rt_csv():
    df_2=pd.DataFrame(columns=pd.MultiIndex.from_product([['5_option2','15_option2','5_option3','15_option3'],['left','right','up']]),index=set(ID))
    for i in range(len(all_csv)):
        option=['15_option2','15_option3','5_option3','5_option2']
        df=pd.read_csv(all_csv[i],encoding="latin1")
        left,right,up=avg_of_exposure_and_rt(df)
        for j in set(ID):
            if j in name[i]:
                csv_id=j
                #break
        for j in option :
            if j == name_1[i]:
                csv_column=j
                #break
        df_2[csv_column,"left"][csv_id]=left
        df_2[csv_column,"right"][csv_id]=right
        df_2[csv_column,"up"][csv_id]=up
    df_2=df_2.fillna(0)
    df_2.to_csv("exposure_and_rt_avg.csv",encoding="latin1")
get_exposure_add_rt_csv()

def get_count_csv():
    df_2=pd.DataFrame(columns=pd.MultiIndex.from_product([['5_option2','15_option2','5_option3','15_option3'],['left','right','up']]),index=set(ID))
    for i in range(len(all_csv)):
        option=['15_option2','15_option3','5_option3','5_option2']
        df=pd.read_csv(all_csv[i],encoding="latin1")
        left,right,up=get_count(df)
        for j in set(ID):
            if j in name[i]:
                csv_id=j
                #break
        for j in option :
            if j == name_1[i]:
                csv_column=j
                #break
        df_2[csv_column,"left"][csv_id]=left
        df_2[csv_column,"right"][csv_id]=right
        df_2[csv_column,"up"][csv_id]=up
    df_2=df_2.fillna(0)
    df_2.to_csv("count.csv",encoding="latin1")
get_count_csv() 