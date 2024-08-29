# -*- coding: utf-8 -*-
"""heart_disease_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14T49y3Iqs-TnxTRmnCvVqKSJwErHgmoH
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data =  pd.read_csv("/content/heart_disease_data.csv")

data.head()

data.tail()

data.shape()

data.shape

data.info()

data.isnull().sum()

data.describe()

data['target'].value_counts()

"""1 - Represents Heart
2 - Represents healthy heart
"""

X = data.drop(columns = 'target', axis = 1)
Y = data['target']

print(X)

print(Y)

"""Splitting the data into traininig data and test data"""

X_train ,X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)



model = LogisticRegression()

model.fit(X_train , Y_train)

"""Accuracy score"""

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print("Acuuracy : ", training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print("Acuuracy : ", test_data_accuracy)

input_data = (37,1,2,130,250,0,1,187,0,3.5,0,0,2)

input_data_as_numpy_array = np.asarray(input_data)
reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(reshaped)

print(prediction)