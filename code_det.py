import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
ds=pd.read_csv('new3.csv')
ds.head()
print(ds)
x=ds.iloc[:,2:5]
x.head()
y=ds.iloc[:,0]
y.head()
from sklearn.model_selection import train_test_split
x_train ,x_test ,y_train ,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
y_test.shape
knnmodel = KNeighborsClassifier(n_neighbors=3)
knnmodel.fit(x_train,y_train)
y_predict1=knnmodel.predict(x_test)
acc=accuracy_score(y_test,y_predict1)
acc
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test.values,y_predict1)
cm
prediction_output=pd.DataFrame(data=[y_test.values,y_predict1],index=['y_test','y_predict1'])
prediction_output.transpose()
prediction_output.iloc[0,:].value_counts()
