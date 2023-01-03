# -*- coding: utf-8 -*-
"""creditcard_logisticregression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1omqGpgux8_GrGDE4VmBsR6MbbKovEkeT

# Import libraries
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

"""# Credit card data"""

from google.colab import drive
drive.mount('/content/gdrive')

PATH = '/content/gdrive/MyDrive/Creditcard_data/creditcard.csv';

dataframe = pd.read_csv(PATH)
dataframe.head(5)

dataframe.shape

"""# Class-imbalance - fraud transactions"""

dataframe['Class'].value_counts()

"""# Logistic regression"""

x = dataframe.drop(['Class'],axis=1)
y = dataframe.Class

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=331, test_size=0.33)

print("train rows: {}, test rows: {}".format(x_train.shape[0], x_test.shape[0]))  # rows

lr = LogisticRegression(solver='lbfgs', max_iter=1000)
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

lr.score(x_test, y_test)

confusion_matrix(y_test, y_pred, labels=[1,0])

tp, fn, fp, tn = confusion_matrix(y_test, y_pred, labels=[1,0]).ravel()
(tp, fn, fp, tn)

sensitivity = tp/(tp+fn)
specificity = tn/(fp+tn)

print("sensitivity = {:.4f}, specificity = {:.4f}".format(sensitivity, specificity))

"""## C 0.25"""

lr = LogisticRegression(solver='lbfgs', max_iter=1000, C=0.25)
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

lr.score(x_test, y_test)

confusion_matrix(y_test, y_pred, labels=[1,0])

tp, fn, fp, tn = confusion_matrix(y_test, y_pred, labels=[1,0]).ravel()
(tp, fn, fp, tn)

sensitivity = tp/(tp+fn)
specificity = tn/(fp+tn)

print("sensitivity = {:.4f}, specificity = {:.4f}".format(sensitivity, specificity))

"""## C 0.5"""

lr = LogisticRegression(solver='lbfgs', max_iter=1000, C=0.5)
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

lr.score(x_test, y_test)

confusion_matrix(y_test, y_pred, labels=[1,0])

tp, fn, fp, tn = confusion_matrix(y_test, y_pred, labels=[1,0]).ravel()
(tp, fn, fp, tn)

sensitivity = tp/(tp+fn)
specificity = tn/(fp+tn)

print("sensitivity = {:.4f}, specificity = {:.4f}".format(sensitivity, specificity))

"""## C 1.0"""

lr = LogisticRegression(solver='lbfgs', max_iter=1000, C=1)
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

lr.score(x_test, y_test)

confusion_matrix(y_test, y_pred, labels=[1,0])

tp, fn, fp, tn = confusion_matrix(y_test, y_pred, labels=[1,0]).ravel()
(tp, fn, fp, tn)

sensitivity = tp/(tp+fn)
specificity = tn/(fp+tn)

print("sensitivity = {:.4f}, specificity = {:.4f}".format(sensitivity, specificity))

"""## C 5.0"""

lr = LogisticRegression(solver='lbfgs', max_iter=1000, C=5)
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

lr.score(x_test, y_test)

confusion_matrix(y_test, y_pred, labels=[1,0])

tp, fn, fp, tn = confusion_matrix(y_test, y_pred, labels=[1,0]).ravel()
(tp, fn, fp, tn)

sensitivity = tp/(tp+fn)
specificity = tn/(fp+tn)

print("sensitivity = {:.4f}, specificity = {:.4f}".format(sensitivity, specificity))

"""## C 20.0"""

lr = LogisticRegression(solver='lbfgs', max_iter=1000, C=20)
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

lr.score(x_test, y_test)

confusion_matrix(y_test, y_pred, labels=[1,0])

tp, fn, fp, tn = confusion_matrix(y_test, y_pred, labels=[1,0]).ravel()
(tp, fn, fp, tn)

sensitivity = tp/(tp+fn)
specificity = tn/(fp+tn)

print("sensitivity = {:.4f}, specificity = {:.4f}".format(sensitivity, specificity))