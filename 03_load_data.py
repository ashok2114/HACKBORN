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
# import modules
import pandas as pd
 
 
# Load dataset
#url = "D:\\mycode\\python\\machine_learning\\iris.data"
url =  os.path.join('Dataset','transactiondata.dat')
url1 =os.path.join('Dataset', 'customermaster.dat')
names = ['cust_id', 'cr_dr', 'amount', 'date', 'status']
names = ['cust_name', 'salary','cust_id']
dataset = pandas.read_csv(url, names=names)
dataset1 = pandas.read_csv(url1, names=names)
 
df1 = pd.DataFrame(dataset, columns = ['cust_id', 'cr_dr', 'amount', 'date', 'status'])
 
df2 = pd.DataFrame(dataset1, columns = ['cust_id', 'salary'])
 
#print(df1)
#print('second dataframe')
#print(df2)
 
 
merge_result=pd.merge(df1, df2, how='outer', on=['cust_id', 'cust_id'])
print(merge_result.sort_index(ascending=[1, 0]))
 
#result = df2.join(df1, on='cust_id')
#print(result)