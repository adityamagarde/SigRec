# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 03:33:23 2017

@author: ADITYA
"""

#IMPORTING DEPENDENCIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'DatasetsCreated/datasetOne.csv')
X = dataset.iloc[:, 0:17].values
y = dataset.iloc[:, -1].values

#splitting the dataset into test and training
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


#feature scaling
from sklearn.preprocessing import StandardScaler
stanScalerX = StandardScaler()
X_train = stanScalerX.fit_transform(X_train)
X_test = stanScalerX.transform(X_test)


#--------------------------------------------------------------------------------------------
#MAKING THE ANN
#importing keras libraries
import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()
classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'relu', input_dim = 17))
#classifier1.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))
classifier.add(Dense(activation='relu', units=6, kernel_initializer='uniform'))
classifier.add(Dense(activation='sigmoid', units=1, kernel_initializer='uniform'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(X_train, y_train, batch_size = 10, epochs = 250)

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


##TESTING THE DATASET ----------------------------------------------------------------------------
testDataset = pd.read_csv(r'DatasetsCreated\testSet.csv', header=None)
Xtesting = testDataset.iloc[:, 0:17].values
Xtesting = stanScalerX.transform(Xtesting)
new_prediction = classifier.predict(Xtesting)
new_predictionBinary = new_prediction
new_predictionBinary[new_predictionBinary > 0.5] = True
new_predictionBinary[new_predictionBinary < 0.5] = False
#
