'''

Only to show how the model was created

'''

import pandas as pd

dataset=pd.read_csv("static/Social_Network_Ads.csv")

#data split
X = dataset.iloc[:,1:4].values
Y = dataset.iloc[:,4:].values

#X preprocessing

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

X[:,0]=le.fit_transform(X[:,0:1])

from sklearn.preprocessing import StandardScaler

std = StandardScaler()

X=std.fit_transform(X)

#Y preprocessing
ley = LabelEncoder()
Y=ley.fit_transform(Y)

#Support Vector Machines

from sklearn.svm import SVC
sv = SVC()
sv.fit(X,Y)

import joblib
joblib.dump(sv,'models/model.pkl')
joblib.dump(le,'models/label.pkl')
joblib.dump(std,'models/std.pkl')