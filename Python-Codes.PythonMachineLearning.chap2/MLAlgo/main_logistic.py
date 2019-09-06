'''
Created on Sep 2, 2019

@author: krish.mahajan@ibm.com
''' 



import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import plot
from LogisticRegression import LogisticRegressionGD 


if __name__ == '__main__': 
      
    df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None) 
    
    y = df.iloc[0:100,4].to_numpy() 
    y = np.where(y =='Iris-setosa',0,1) 
    
    X = df.iloc[0:100,[0,2]].to_numpy()   
    
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    
    lr = LogisticRegressionGD(n_iter=1000, eta=0.01)
    lr.fit(X_std, y) 
    
    plot.plot_decision_regions(X=X_std,y=y,classifier = lr) 
    plt.xlabel('Petal Length') 
    plt.xlabel('Petal width') 
    plt.legend(loc='upper left')
    plt.show()

   


if __name__ == '__main__':
    pass