import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn import decomposition
from sklearn import datasets

# load dataset into Pandas DataFrame
df = pd.read_csv("D:\Python_programs\ML\Complete_Data_.csv")

from sklearn.preprocessing import StandardScaler
n=[]
ind=[]
for i in range(200):
    n.append(i+1)
for i in range(200):
    ind.append('px'+str(n[i]))

features = ind
X = df.loc[:, features].values
# Separating out the target
Y = df.loc[:,['target']].values
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
 X, Y, test_size = 0.3, random_state = 100)
y_train=y_train.ravel()
y_test=y_test.ravel()
#classifier.fit(X_train, y_train.squeeze())

from sklearn.neighbors import KNeighborsClassifier  # FOR K=13 ,IT HAS ACCURACY AROUND 72.7488902980
from sklearn import metrics
import time
#model = KNeighborsClassifier()
model=KNeighborsClassifier(n_neighbors =13, weights='uniform', algorithm='auto')
model.fit(X_train, y_train)
start = time.time()
Yhat = model.predict(X_test)
end = time.time()
print('Time Taken For Classification is :',(end - start))
print("Accuracy :",metrics.accuracy_score(Yhat, y_test)*100)
print('\n','*'*11,'Accuracy of INDIAN-PINES Dataset Before PCA','*'*11)
print('*'*11,' Classifier : K-NEAREST NEIGHBOUR ','*'*11)
for K in range(25):
 K_value = K+1
 neigh = KNeighborsClassifier(n_neighbors = K_value, weights='uniform', algorithm='auto')
 neigh.fit(X_train, y_train) 
 y_pred = neigh.predict(X_test)
 print ("Accuracy is :%1.10f"%(metrics.accuracy_score(y_test,y_pred)*100),"% ","for K-Value: %4d"%(K_value))

