# -*- coding: utf-8 -*-
"""creditcard_knn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gz5F401q0zNTP1237Q1ImgIhdON6mdWf

### Import libraries
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

"""### Credit card data"""

from google.colab import drive
drive.mount('/content/gdrive')

PATH = '/content/gdrive/MyDrive/Creditcard_data/creditcard.csv';

dataframe = pd.read_csv(PATH)
dataframe.head(5)

dataframe.shape

"""### Class-imbalance - fraud transactions"""

dataframe['Class'].value_counts()

"""### K-Nearest Neighbor Classifier"""

x = dataframe.drop(['Class'],axis=1)
y = dataframe.Class

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=331, test_size=0.33)

print("train rows: {}, test rows: {}".format(x_train.shape[0], x_test.shape[0]))  # rows

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

knn.score(x_test, y_test)

confusion_matrix(y_test, y_pred, labels=[1,0])

tp, fn, fp, tn = confusion_matrix(y_test, y_pred, labels=[1,0]).ravel()
(tp, fn, fp, tn)

sensitivity = tp/(tp+fn)
specificity = tn/(fp+tn)

print("sensitivity = {:.4f}, specificity = {:.4f}".format(sensitivity, specificity))