#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://developer.51cto.com/art/201507/485276.htm
import numpy as np
import urllib


def analysis_pre(url='file:///E:/rthings/code/python/weibo/bigdata/vector/vector.html',
                 dimension_num=16):
    # url = 'file:///E:/rthings/code/python/weibo/output/list_num/list_num.html'
    raw_data = urllib.urlopen(url)
    # load the CSV file as a numpy matrix
    dataset = np.loadtxt(raw_data, delimiter="\t")
    # separate the data from the target attributes
    X = dataset[:, 1:dimension_num - 1]
    y = dataset[:, :1]
    return X, y


def analysis_method(method='svm', X=None, y=None):
    if str(method) == 'svm':
        analysis_svm(X=X, y=y)
        return
    if str(method) == 'beyes':
        analysis_beyes(X=X, y=y)
        return
    if str(method) == 'cart':
        analysis_cart(X=X, y=y)
        return
    if str(method) == 'knn':
        analysis_knn(X=X, y=y)
        return
    analysis_svm(X=X, y=y)
    return


def analysis_svm(X=None, y=None):
    print "----------SVM-----------------------"
    from sklearn import metrics
    from sklearn.svm import SVC
    # fit a SVM model to the data
    model = SVC()
    model.fit(X, y)
    print(model)
    # make predictions
    expected = y
    predicted = model.predict(X)
    # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))


def analysis_beyes(X=None, y=None):
    from sklearn import metrics
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(X, y)
    print(model)
    # make predictions
    expected = y
    predicted = model.predict(X)
    # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))


def analysis_cart(X=None, y=None):
    from sklearn import metrics
    from sklearn.tree import DecisionTreeClassifier
    # fit a CART model to the data
    model = DecisionTreeClassifier()
    model.fit(X, y)
    print(model)
    # make predictions
    expected = y
    predicted = model.predict(X)
    # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))


def analysis_knn(X=None, y=None):
    from sklearn import metrics
    from sklearn.neighbors import KNeighborsClassifier
    # fit a k-nearest neighbor model to the data
    model = KNeighborsClassifier()
    model.fit(X, y)
    print(model)
    # make predictions
    expected = y
    predicted = model.predict(X)
    # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
