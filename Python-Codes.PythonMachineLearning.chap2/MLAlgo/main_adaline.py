'''
Created on Aug 30, 2019

@author: krish.mahajan@ibm.com
'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from AdalineSGD import AdalineSGD


if __name__ == '__main__': 
      
    df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None) 
    
    y = df.iloc[0:100,4].to_numpy() 
    y = np.where(y =='Iris-setosa',-1,1) 
    
    X = df.iloc[0:100,[0,2]].to_numpy()   
    
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    
    ada = AdalineSGD(n_iter=15, eta=0.01)
    ada.fit(X_std, y)
    
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Sum-squared-error')

    plt.tight_layout()
# plt.savefig('./adaline_3.png', dpi=300)
    plt.show()
   