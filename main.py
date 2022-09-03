
import pickle
import sklearn

import pandas as pd
import numpy as np
admindata = pd.read_csv('admission_data.csv')

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(admindata[['GRE Score','TOEFL Score','University Rating','SOP','LOR','CGPA','Research']], admindata.Admit, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)

from sklearn import svm
clf = svm.SVC()
clf.fit(X_train, y_train)

Xnew = [[350,190,3,3,3.5,8,1]]
ynew = model.predict(Xnew)
print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))

#filename = 'finalized_model.sav'
#model = pickle.load(open(filename, 'rb'))

#Xnew = [[50,100,3,3,3.5,8,1]]
#ynew = model.predict(Xnew)
#print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))



