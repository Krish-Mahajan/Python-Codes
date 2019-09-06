'''
Created on Aug 30, 2019

@author: krish.mahajan@ibm.com
''' 

import numpy as np

class Perceptron(object):
    '''
    Perceptron classifier  
    
    
    parameters
    ------------ 
    
    eta : float 
        Learning rate ( between 0.0 and 1.0) 
    n_iter : int
        passes over the training dataset 
    random_state : int 
        random number genrator seed for random weight initialization
        
        
    Attributes
    ----------- 
    
    w_ : 1d-array
        weights after fitting 
    errors_ : list 
        NUmber of misclassifications (updates) in each epoch.
    
    '''


    def __init__(self ,eta = 0.0, n_iter=50, shuffle= True,random_state =1):
        self.eta = eta 
        self.n_iter = n_iter 
        self.random_state = random_state 
        self.shuffle = shuffle
        
        
    def fit(self,X,y): 
        '''
        Fit training data 
        
        parameters 
        ----------- 
        X : {array-like } , shape = [n_samples,n_features] 
        Training vectors , where n_samples is the number of samples . 
        
        Y : {array-like} , shape = [n_samples] 
        Training values 
        
        Returns
        -------- 
        self : object 
        ''' 
        rgen = np.random.RandomState(self.random_state) 
        self.w_ = rgen.normal(loc=0.0 , scale=0.01,size = 1 + X.shape[1]) 
        
        self.errors_ = [] 
        
        for _ in range(self.n_iter): 
            if self.shuffle :
                X , y = self._shuffle(X,y)
            errors = 0 
            for xi , target in zip(X,y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update 
                errors += int(update != 0.0)
            self.errors_.append(errors)
        
        return self  
    
    def _shuffle(self,X,y):
        '''
        shuffling traning data
        '''
        r = np.random.permutation(len(y))
        return X[r],y[r]
    
    def net_input(self,Xi): 
        '''
        calculate the net input
        '''
        return np.dot(self.w_[1:],Xi) + self.w_[0] 
    
    def predict(self,Xi):
        '''
        returns class label
        '''
        return np.where(self.net_input(Xi) >= 0.0 , 1 , -1)
        
        
        
        
        