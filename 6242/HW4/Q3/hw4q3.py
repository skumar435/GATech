## Data and Visual Analytics - Homework 4
## Georgia Institute of Technology
## Applying ML algorithms to detect eye state

import numpy as np
import pandas as pd
import time

from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate, train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA

######################################### Reading and Splitting the Data ###############################################
# XXX
# TODO: Read in all the data. Replace the 'xxx' with the path to the data set.
# XXX
data = pd.read_csv('eeg_dataset.csv')

# Separate out the x_data and y_data.
x_data = data.loc[:, data.columns != "y"]
y_data = data.loc[:, "y"]

# The random state to use while splitting the data.
random_state = 100

# XXX
# TODO: Split 70% of the data into training and 30% into test sets. Call them x_train, x_test, y_train and y_test.
# Use the train_test_split method in sklearn with the parameter 'shuffle' set to true and the 'random_state' set to 100.
# XXX
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.30, random_state=100, shuffle=True)

# ############################################### Linear Regression ###################################################
# XXX
# TODO: Create a LinearRegression classifier and train it.
# XXX
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

# XXX
# TODO: Test its accuracy (on the training set) using the accuracy_score method.
# TODO: Test its accuracy (on the testing set) using the accuracy_score method.
# Note: Round the output values greater than or equal to 0.5 to 1 and those less than 0.5 to 0. You can use y_predict.round() or any other method.
# XXX
y_tr_predict = lin_reg.predict(x_train)
print("LRScore train: {}".format(accuracy_score(y_train, y_tr_predict.round())))
y_test_predict = lin_reg.predict(x_test)
print("LRScore test: {}".format(accuracy_score(y_test, y_test_predict.round())))

# ############################################### Random Forest Classifier ##############################################
# XXX
# TODO: Create a RandomForestClassifier and train it.
# XXX
rfcl = RandomForestClassifier()
rfcl.fit(x_train, y_train)

# XXX
# TODO: Test its accuracy on the training set using the accuracy_score method.
# TODO: Test its accuracy on the test set using the accuracy_score method.
# XXX
y_tr_clf_predict = rfcl.predict(x_train)
print("RFScore train: {}".format(accuracy_score(y_train, y_tr_clf_predict)))
y_test_clf_predict = rfcl.predict(x_test)
print("RFScore test: {}".format(accuracy_score(y_test, y_test_clf_predict)))

# XXX
# TODO: Determine the feature importance as evaluated by the Random Forest Classifier.
#       Sort them in the descending order and print the feature numbers. The report the most important and the least important feature.
#       Mention the features with the exact names, e.g. X11, X1, etc.
#       Hint: There is a direct function available in sklearn to achieve this. Also checkout argsort() function in Python.
# XXX
feature_importances = pd.DataFrame(rfcl.feature_importances_,
                                   index = x_train.columns,
                                    columns=['importance']).sort_values('importance', ascending=False)
print(feature_importances)

# XXX
# TODO: Tune the hyper-parameters 'n_estimators' and 'max_depth'.
#       Print the best params, using .best_params_, and print the best score, using .best_score_.
# Get the training and test set accuracy values after hyperparameter tuning.
# XXX
parameters_rf = {'max_depth':[10, 15, 20], 'n_estimators':[15, 40, 65]}
clf1 = GridSearchCV(rfcl, parameters_rf, cv=10)
clf1.fit(x_train, y_train)
print("RF Best Params: {}".format(clf1.best_params_))
print("RF Best Score: {}".format(clf1.best_score_))
y_test_predict_rfcv = clf1.predict(x_test)
print("RFScore test GridCV: {}".format(accuracy_score(y_test, y_test_predict_rfcv)))

# ############################################ Support Vector Machine ###################################################
# XXX
# TODO: Pre-process the data to standardize or normalize it, otherwise the grid search will take much longer
# TODO: Create a SVC classifier and train it.
# XXX
scaler = StandardScaler()
scaler.fit(x_train)
x_train_st = scaler.transform(x_train)
x_test_st = scaler.transform(x_test)
svclf = SVC(gamma='scale')
svclf.fit(x_train_st, y_train)

# XXX
# TODO: Test its accuracy on the training set using the accuracy_score method.
# TODO: Test its accuracy on the test set using the accuracy_score method.
# XXX
y_tr_svc_predict = svclf.predict(x_train_st)
print("SVMScore train: {}".format(accuracy_score(y_train, y_tr_svc_predict)))
y_test_svc_predict = svclf.predict(x_test_st)
print("SVMScore test: {}".format(accuracy_score(y_test, y_test_svc_predict)))

# XXX
# TODO: Tune the hyper-parameters 'C' and 'kernel' (use rbf and linear).
#       Print the best params, using .best_params_, and print the best score, using .best_score_.
# Get the training and test set accuracy values after hyperparameter tuning.
# XXX
parameters_svc = {'kernel':['linear', 'rbf'], 'C':[0.1, 1, 10]}
clf2 = GridSearchCV(svclf, parameters_svc, cv=10)
clf2.fit(x_train_st, y_train)
print("SVM Best Params: {}".format(clf2.best_params_))
print("SVM Best Score: {}".format(clf2.best_score_))
y_test_predict_svmcv = clf2.predict(x_test_st)
print("SVMScore test GridCV: {}".format(accuracy_score(y_test, y_test_predict_svmcv)))

# XXX
# TODO: Calculate the mean training score, mean testing score and mean fit time for the 
# best combination of hyperparameter values that you obtained in Q3.2. The GridSearchCV 
# class holds a  ‘cv_results_’ dictionary that should help you report these metrics easily.
# XXX
print("Mean test score: {}".format(clf2.cv_results_['mean_test_score'][clf2.best_index_]))
print("Mean training score: {}".format(clf2.cv_results_['mean_train_score'][clf2.best_index_]))
print("Mean fit time: {}".format(clf2.cv_results_['mean_fit_time'][clf2.best_index_]))

# ######################################### Principal Component Analysis #################################################
# XXX
# TODO: Perform dimensionality reduction of the data using PCA.
#       Set parameters n_component to 10 and svd_solver to 'full'. Keep other parameters at their default value.
#       Print the following arrays:
#       - Percentage of variance explained by each of the selected components
#       - The singular values corresponding to each of the selected components.
# XXX
pca = PCA(n_components=10, svd_solver='full')
pca.fit(x_data)
print("Percentage of variance: {}".format(pca.explained_variance_ratio_))
print("Singular values: {}".format(pca.singular_values_))