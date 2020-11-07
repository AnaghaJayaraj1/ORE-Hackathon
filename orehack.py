from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

df=pd.read_csv('employee.csv',sep=',') #Reading the given data


X = df[['commskill','ethics','knowledge','job']]


y = df['overall']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)

model = LinearRegression()
model.fit(X_train,Y_train)

predictions= model.predict(X_test)

print('accuracy ', model.score(X_test,y_test)*100,'%')