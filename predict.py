#Import Library of Gaussian Naive Bayes model
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Load dataset
url = "A:/Machine_Learning/naivesample/transactiondata.data"
names = ['account-no', 'credit-debit', 'amount', 'date', 'comment']
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset new
array = dataset.values
X = array[:,0:4]
Y = array[:,0]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

 
#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets 
model.fit(X_train, Y_train)

#Predict Output 
predictions= model.predict(X_validation)
print(predictions)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))