import pandas as pd
import numpy as np
import pickle
import warnings
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators=1000,random_state=14)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
warnings.filterwarnings("ignore")

dataset=pd.read_csv('cpdata.csv',delimiter=",")
X = dataset[['temperature', 'humidity', 'ph', 'rainfall']].values
y = dataset["label"]

label= pd.get_dummies(dataset.label).iloc[: , 1:]
dataset= pd.concat([dataset,label],axis=1)
dataset.drop('label', axis=1,inplace=True)
train=dataset.iloc[:, 0:4].values
test=dataset.iloc[: ,4:].values

X_train,X_test,y_train,y_test=train_test_split(train,test,test_size=0.3)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

rf.fit(X_train,y_train)
randomTest=rf.predict(X_test)

pickle.dump(rf,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))











