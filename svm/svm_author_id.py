#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

#########################################################
### your code goes here ###

from sklearn.svm import SVC

for C in [10000.,]:  # [10.0, 100., 1000., 10000.]
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
    print 'accuracy = ', accuracy    #  = 0.973833902162
    print '.' * 30
    #C = [10, 26, 50]
    #for i in range(len(C)):
    #    print 'pred[',C[i],'] = ', pred[C[i]]

    print '# in Chris class = ', pred.sum()

#########################################################


