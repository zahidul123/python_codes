import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

dataset=pd.read_csv(r'F:\havingnewinPython\machineLearning\Sandextutorial\50_Startups.csv')
x=dataset.iloc[:,:-1]#it only shows column from first to last-1
y=dataset.iloc[:,4]#it only shows column number 4

states=pd.get_dummies(x['State'],drop_first=True) #it made all string variable into 0 and 1 dummy
x=x.drop('State',axis=1) #we just drop state column

x=pd.concat([x,states],axis=1) #add the dummy variable

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)#we split data for train 20%

from sklearn.linear_model import LinearRegression
regression=LinearRegression()

regression.fit(x_train,y_train)
val=pd.DataFrame(np.array([[66051.52],[182645.56],[118148.20],[1],[1]])
                 ,columns=['R&D Spend','Administration','Marketing Spend','New York','California'])
predicct=regression.predict(val)
print(predicct)
print(x_test)
from sklearn.metrics import r2_score
score=r2_score(y_test,predicct)
print(score)

