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
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:,['target']].values
# Standardizing the features
from sklearn.preprocessing import MinMaxScaler
scaler_model = MinMaxScaler()
scaler_model.fit(x.astype(float))
x=scaler_model.transform(x)


from sklearn.decomposition import PCA


## Finding the principle components
pca = PCA(n_components=10)
principalComponents = pca.fit_transform(x)
ev=pca.explained_variance_ratio_

# *Since the initial 2 principal components have high variance.
#   so, we select pc-1 and pc-2.
#---------------------------------------------------
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['PC-1','PC-2'])
# Adding lables
finalDf = pd.concat([principalDf, df[['target']]], axis = 1)

#--------- Bar Graph for Explained Variance Ratio ------------
plt.bar([1,2,3,4,5,6,7,8,9,10],list(ev*100),label='Principal Components',color='b')
plt.legend()
plt.xlabel('Principal Components')
pc=[]
for i in range(10):
    pc.append('PC'+str(i+1))
#plt.xticks([1,2,3,4,5,6,7,8,9,10],pc, fontsize=8, rotation=30)
plt.xticks([1,2,3,4,5,6,7,8,9,10],pc, fontsize=8, rotation=30)
plt.ylabel('Variance Ratio')
plt.title('Variance Ratio of INDIAN PINES Dataset')
plt.show()


#---------------------------------------------------
# Plotting pc1 & pc2
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('PC-1', fontsize = 15)
ax.set_ylabel('PC-2', fontsize = 15)
ax.set_title('PCA on INDIAN PINES Dataset', fontsize = 20)
targets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
colors = ['r','g','b','y','m','c','k','r','g','b','y','m','c','k','b','r']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'PC-1']
               , finalDf.loc[indicesToKeep, 'PC-2']
               , c = color
               , s = 9)
ax.legend(targets)
ax.grid()
plt.show() # FOR SHOWING THE PLOT

#-------------------SENDING REDUCED DATA INTO CSV FILE------------

finalDf.to_csv('indian_pines_after_pca.dat')

