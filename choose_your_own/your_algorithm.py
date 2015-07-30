#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
'''
# Naive Bayes
import numpy as np
from sklearn.naive_bayes import GaussianNB
### create classifier
clf = GaussianNB()
### fit the classifier on the training features and labels
t0 = time()
clf.fit(features_train, labels_train)
print 'training time:', round(time() - t0, 3), 's'
### use the trained classifier to predict labels for the test features
t0 = time()
pred = clf.predict(features_test)
print 'prediction time:', round(time() - t0, 3), 's'
### calculate and return the accuracy on the test data
accuracy = (1. * (pred == labels_test)).sum() / float(len(pred))
print 'accuracy = ', accuracy    

# SVM
from sklearn.svm import SVC
### create classifier
for C in [10.0, 100., 1000., 10000., 100000., 1000000.]:  # 
    clf = SVC(kernel="rbf", C=C)
    print '.' * 50
    print 'C = ', C
    t0 = time()
    clf.fit(features_train, labels_train)
    print 'Train time:', round(time() - t0, 3), 's'
    t0 = time()
    pred = clf.predict(features_test)
    print 'Prediction time:', round(time() - t0, 3), 's'
    accuracy = (1. * (pred == labels_test)).sum() / float(len(pred))
    print 'accuracy = ', accuracy   

# Decision Trees
from sklearn import tree
for S in [20,]:   # [10:100] --> near 20 is optimial
    print '.' * 50
    print 'S = ', S  # S = min(# instances) to split a node.
    clf = tree.DecisionTreeClassifier(min_samples_split = S)
    t0 = time()
    clf.fit(features_train, labels_train)
    print 'Train time:', round(time() - t0, 3), 's'
    t0 = time()
    pred = clf.predict(features_test)
    print 'Prediction time:', round(time() - t0, 3), 's'
    acc = accuracy_score(labels_test, pred)
    print 'accuracy =', acc

# KNN
from sklearn.neighbors import KNeighborsClassifier
for L in [30,]:   # 30 works fine (the default)
    print '.' * 50
    #print 'N = ', N  #   N = number of neighbors
    print 'L = ', L  #   L = leaf size
    clf = KNeighborsClassifier(n_neighbors = 20, leaf_size = L)
    t0 = time()
    clf.fit(features_train, labels_train)
    print 'Train time:', round(time() - t0, 3), 's'
    t0 = time()
    pred = clf.predict(features_test)
    print 'Prediction time:', round(time() - t0, 3), 's'
    acc = accuracy_score(labels_test, pred)
    print 'accuracy =', acc

# Random Forest
from sklearn.ensemble import RandomForestClassifier
for N in [7,]:   # 10 is the default
    print '.' * 50
    print 'N = ', N  #   N = number of estimators (# trees in forest)
    clf = RandomForestClassifier(n_estimators = N)
    t0 = time()
    clf.fit(features_train, labels_train)
    print 'Train time:', round(time() - t0, 3), 's'
    t0 = time()
    pred = clf.predict(features_test)
    print 'Prediction time:', round(time() - t0, 3), 's'
    acc = accuracy_score(labels_test, pred)
    print 'accuracy =', acc
'''

# Adaboost
from sklearn.ensemble import AdaBoostClassifier
for N in [50,]:   # 50 is the default
    print '.' * 50
    print 'N = ', N  #   N = number of estimators (# trees in forest)
    clf = AdaBoostClassifier(n_estimators = N)
    t0 = time()
    clf.fit(features_train, labels_train)
    print 'Train time:', round(time() - t0, 3), 's'
    t0 = time()
    pred = clf.predict(features_test)
    print 'Prediction time:', round(time() - t0, 3), 's'
    acc = accuracy_score(labels_test, pred)
    print 'accuracy =', acc


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
