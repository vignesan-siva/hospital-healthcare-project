import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv("C:\\Users\\elcot\\Desktop\\machine learning tutorial\\hospital_project\\SugarPrediction.csv")

x=data.iloc[:,[0,4,6,9]].values
y=data.iloc[:,[-1]].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.ensemble import RandomForestRegressor
classifier=RandomForestRegressor()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)





