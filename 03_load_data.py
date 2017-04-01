# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from itertools import groupby
import os
from sklearn.covariance import EmpiricalCovariance, MinCovDet,EllipticEnvelope
# import modules
import pandas as pd
 
 
# Load dataset
#url = "D:\\mycode\\python\\machine_learning\\iris.data"
url =  os.path.join('Dataset','transactiondata.dat')
url1 =os.path.join('Dataset', 'customermaster.dat')
names = ['cust_id', 'cr_dr', 'amount', 'date', 'status']
names1 = ['cust_name', 'salary','cust_id']
dataset = pandas.read_csv(url, names=names)
dataset1 = pandas.read_csv(url1, names=names1)

#print(dataset.shape)
#print(dataset1.shape)
 
df1 = pd.DataFrame(dataset, columns = ['cust_id', 'cr_dr', 'amount', 'date', 'status'])
 
df2 = pd.DataFrame(dataset1, columns = ['cust_id', 'salary'])
 
#print(df1)
#print('second dataframe')
#print(df2)
 
 
merge_result=pd.merge(df1, df2, how='outer', on=['cust_id', 'cust_id'])

results = (merge_result.sort_index(ascending=[1, 0]))
#print (results.shape)
#print(results.describe())
 
#result = df2.join(df1, on='cust_id')
#print(results)

## apply elliptic envelope covariance on the data set
#results.to_csv("results.dat")


#we have the final data set with us, with dimension salary added to transaction data
#With salary dimension added, this data set is assumed to be Gaussian normal distribution 
# With this assumption, and since we have a contaminated data set , we will do a outliers analysis on the dataset
#We will fit the data points in a elliptic envelope, and try to predict outliers on a selected data set

outlier_analysis = EllipticEnvelope(contamination=0.1).fit(results)
# predict if the dataset is valid, by taking a training set as 1
outlier_analysis.predict(results.head(1))
#########
#need to fix the error in fit call
