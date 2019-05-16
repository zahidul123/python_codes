#picklink is a serilization of python in dictonary

import pandas as pd
import numpy as np
import math
from sklearn import svm,preprocessing,cross_validation
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')
df=pd.read_csv(r'F:\havingnewinPython\machineLearning\Sandextutorial\stock.csv',header=0, index_col='Date',parse_dates=True)

df=df[['Adj_Open','Adj_High','Adj_Low','Adj_Close','Adj_Volume',]]
df['HL_PCT']=(df['Adj_High']- df['Adj_Low'])/df['Adj_Low'] *100.0
df['PCT_Change']=(df['Adj_Close']-df['Adj_Open'])/df['Adj_Open'] *100.0
df=df[['Adj_Close','HL_PCT','PCT_Change','Adj_Volume']]#it help to append
print(len(df))

df.fillna(value=-1,inplace=True)
forecast_out=int(math.ceil(.02*len(df)))
df['label']=df['Adj_Close'].shift(-forecast_out)
#df.dropna(inplace=True)
print(df.head())

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

#clf = LinearRegression(n_jobs=-1)
#clf.fit(X_train, y_train)
#with open('linearregression.pickle','wb') as f:
#    pickle.dump(clf, f)

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)

confidence = clf.score(X_test, y_test)
print(confidence)

forecast_set = clf.predict(X_lately)
print(forecast_set, confidence, forecast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day


for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj_Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
