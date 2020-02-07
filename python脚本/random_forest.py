# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:42:19 2019

@author: HASEE
"""
import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
month=["01","02","03","04","05","06","07","08","09","10","11","12"]
year=["2015","2016","2017"]
"""
for m in month:
    for y in year:
        with open("重庆市-station_realtime-"+y+"-"+m+".csv",encoding="utf-8") as f:
            df=pd.read_csv(f)
            df.pop("province")
            df.pop("city")
            df.pop("city_code")
            df.pop("station")
            df.pop("station_code")
            df.pop("index")
            df.pop("so2_24h")
            df.pop("no2_24h")
            df.pop("co_24h")
            df.pop("o3_24h")
            df.pop("pm10_24h")
            df.pop("pm2_5_24h")
            df.pop("o3_8h_24h")
            df=df.fillna(0)
            df.to_csv("all_data.csv",mode="a")
data=pd.read_csv('all_data.csv',index_col=0,encoding='utf-8')
"""

with open ("重庆市-station_realtime-2014-05.csv",encoding="UTF-8" )as f:
    df=pd.read_csv(f)
    print(df.iloc[0:5,0:8])
    df.pop("province")
    df.pop("city")
    df.pop("city_code")
    df.pop("station")
    df.pop("station_code")
    df.pop("index")
    df.pop("so2_24h")
    df.pop("no2_24h")
    df.pop("co_24h")
    df.pop("o3_24h")
    df.pop("pm10_24h")
    df.pop("pm2_5_24h")
    df.pop("o3_8h_24h")
    df=df.fillna(0)
    df.to_csv("result.csv")
data=pd.read_csv('result.csv',index_col=0,encoding='utf-8')
data=data.sort_values(by="pubtime",ascending=True)
data.pop("level")
data.pop("pollutions")
print (data.head())
print (data.shape)
index=data.index
col=data.columns
class_names=np.unique(data.ix[:,-1])
print (class_names)

#data preprocessing
data_train, data_test= train_test_split(data,test_size=0.1, random_state=0)
X_train=data_train.iloc[:,0:-2]
X_test=data_test.iloc[:,0:-2]
feature=data_train.iloc[:,0:-2].columns
print (feature)
y_train=data_train.iloc[:,-2]
y_test=data_test.iloc[:,-2]

#visual analysis
sns.set(style="ticks", color_codes=True)
palette = sns.xkcd_palette(['dark blue', 'dark green', 'gold', 'orange'])
sns.pairplot(data.drop([u'aqi'],axis = 1), diag_kind = 'kde', plot_kws=dict(alpha = 0.7))
plt.show()

#model building
"""
from sklearn.model_selection import RandomizedSearchCV
criterion=['mse','mae']
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]#stop=2000
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(10, 100, num = 10)]
max_depth.append(None)
min_samples_split = [2, 5, 10]
min_samples_leaf = [1, 2, 4]
bootstrap = [True, False]
random_grid = {'criterion':criterion,
                'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

clf= RandomForestRegressor()
clf_random = RandomizedSearchCV(estimator=clf, param_distributions=random_grid,
                              n_iter = 3,  
                              cv = 3, verbose=2, random_state=42, n_jobs=1)
#get best paras
clf_random.fit(X_train, y_train)
print (clf_random.best_params_)
"""
#error analysis
rf=RandomForestRegressor(criterion='mae',bootstrap=False,max_features='auto', max_depth=80,min_samples_split=4, n_estimators=200,min_samples_leaf=4)
rf.fit(X_train, y_train) 
y_train_pred=rf.predict(X_train)
y_test_pred=rf.predict(X_test)

from sklearn.metrics import mean_squared_error,explained_variance_score,mean_absolute_error,r2_score
print ("决策树模型评估--训练集：")
print ('训练r^2:',rf.score(X_train,y_train))
print ('均方差',mean_squared_error(y_train,y_train_pred))
print ('绝对差',mean_absolute_error(y_train,y_train_pred))
print ('解释度',explained_variance_score(y_train,y_train_pred))

print ("决策树模型评估--验证集：")
print ('验证r^2:',rf.score(X_test,y_test))
print ('均方差',mean_squared_error(y_test,y_test_pred))
print ('绝对差',mean_absolute_error(y_test,y_test_pred))
print ('解释度',explained_variance_score(y_test,y_test_pred))

with open ("重庆市-station_realtime-2014-06.csv",encoding="UTF-8" )as f1:
    df1=pd.read_csv(f1)    
df1.pop("province")
df1.pop("city")
df1.pop("city_code")
df1.pop("station")
df1.pop("station_code")
df1.pop("index")
df1.pop("so2_24h")
df1.pop("no2_24h")
df1.pop("co_24h")
df1.pop("o3_24h")
df1.pop("pm10_24h")
df1.pop("pm2_5_24h")
df1.pop("o3_8h_24h")
df1.pop("level")
df1.pop("pollutions")
df1=df1.sort_values(by="pubtime",ascending=True)
df1.pop("pubtime")
df1 = df1.fillna(0)
df1.to_csv("result2.csv")
data_pred=pd.read_csv('result2.csv',index_col=0,encoding='gb2312')
#data_pred.pop("pubtime")
data_pred.pop("aqi")
index=data_pred.index
y_pred=rf.predict(data_pred.values)
result_reg=pd.DataFrame(index)
result_reg['AQI']=y_pred*10
result_reg.to_csv('predict_result.csv',encoding='gb2312')
print (result_reg)
X_train['aqi'].hist().get_figure()
#X_train['pm10'].hist().get_figure()
iris = datasets.load_iris()
X = iris.data
y = iris.target
y = label_binarize(y, classes=[0, 1, 2])
n_classes = y.shape[1]
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5,random_state=0)
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,
                                 random_state=random_state))
y_score = classifier.fit(X_train, y_train).decision_function(X_test)
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
plt.figure()
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=2, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC')
plt.legend(loc="lower right")
plt.show()

