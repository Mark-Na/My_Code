# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:21:25 2020

@author: sorina
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data_banknote_authentication.txt')
X = dataset.iloc[:, :2].values
t = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, t_train, t_test = train_test_split(X, t, test_size = 1/4, random_state = 87)

print(X_train.shape)
print(X_test.shape)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#training logistic regression
from sklearn.linear_model import LogisticRegression
log = LogisticRegression(random_state = 0)
log.fit(X_train, t_train)

#computing prediction on training set
t_pred_train = log.predict(X_train)
#print(np.concatenate((t_pred_train.reshape(len(t_pred_train),1), t_train.reshape(len(t_train),1)),1))
from sklearn.metrics import confusion_matrix, accuracy_score
cm_train = confusion_matrix(t_train, t_pred_train)
print(cm_train)
accuracy_score(t_train, t_pred_train)

#computing prediction on test set
t_pred_test = log.predict(X_test)
cm = confusion_matrix(t_test, t_pred_test)
print(cm)
accuracy_score(t_test, t_pred_test)

#training svm
from sklearn.svm import SVC
sv = SVC(kernel = 'linear', random_state = 0)
sv.fit(X_train, t_train)

#computing prediction on training set
t_pred_train = sv.predict(X_train)
#print(np.concatenate((t_pred_train.reshape(len(t_pred_train),1), t_train.reshape(len(t_train),1)),1))
cm_train = confusion_matrix(t_train, t_pred_train)
print(cm_train)
accuracy_score(t_train, t_pred_train)

#computing prediction on test set
t_pred_test = sv.predict(X_test)
#print(np.concatenate((t_pred.reshape(len(t_pred),1), t_test.reshape(len(t_test),1)),1))
cm = confusion_matrix(t_test, t_pred_test)
print(cm)
accuracy_score(t_test, t_pred_test)

#SVM with gaussian kernel
C = 1.0
nsv = SVC(kernel='rbf', gamma=0.7, C=C)
#clf = SVC(kernel='poly', degree=4, C=C, gamma='auto')
nsv.fit(X_train, t_train)

#accuracy on training set
t_pred_train = nsv.predict(X_train)
cm_train = confusion_matrix(t_train, t_pred_train)
print(cm_train)
accuracy_score(t_train, t_pred_train)

#accuracy on test set
t_pred_test = nsv.predict(X_test)
cm = confusion_matrix(t_test, t_pred_test)
print(cm)
accuracy_score(t_test, t_pred_test)

#visualization on training set
from matplotlib.colors import ListedColormap
X_set, y_set = sc.inverse_transform(X_train), t_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.1),
                     np.arange(start = X_set[:, 1].min() - 6, stop = X_set[:, 1].max() + 5, step = 0.1))
fig = plt.figure(figsize=(10,8))
plt.contourf(X1, X2, nsv.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('orange', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Training set)')
plt.xlabel('variance of image')
plt.ylabel('skewnessy')
plt.legend()
plt.show()

#visualization on test set
from matplotlib.colors import ListedColormap
X_set, y_set = sc.inverse_transform(X_test), t_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.1),
                     np.arange(start = X_set[:, 1].min() - 6, stop = X_set[:, 1].max() + 5, step = 0.1))
fig = plt.figure(figsize=(10,8))
plt.contourf(X1, X2, nsv.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('orange', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Test set)')
plt.xlabel('variance of image')
plt.ylabel('skewnessy')
plt.legend()
plt.show()