'''
Created on Aug 30, 2019

@author: krish.mahajan@ibm.com
'''
import numpy as np

class AdalineBGD(object):
    '''
    Adaptive Linear Neuron Classifier 
    
    Parameters 
    ---------
    eta : float 
        Learning rate (between 0.0 and 1.0) 
    n_inter : int 
        passes over the training dataset.
        
    Attributes
    ---------- 
    w_ : 1d-array 
        weights after fitting
    cost_ : list 
        sum of squares cost function value in each epocj 
    
    '''


    def __init__(self,eta =0.01 , n_iter = 50,random_state =1):
        self.eta = eta 
        self.n_iter = n_iter 
        self.random_state = random_state
        
    def fit(self,X,y):
        """
        Fit training data 
              parameters 
        ----------- 
        X : {array-like } , shape = [n_samples,n_features] 
        Training vectors , where n_samples is the number of samples . 
        
        Y : {array-like} , shape = [n_samples] 
        Training values 
        
        Returns
        -------- 
        self : object        parameters 
        ----------- 
        X : {array-like } , shape = [n_samples,n_features] 
        Training vectors , where n_samples is the number of samples . 
        
        Y : {array-like} , shape = [n_samples] 
        Training values 
        
        Returns
        -------- 
        self : object 
        """ 
        
        rgen = np.random.RandomState(self.random_state) 
        self.w_ = rgen.normal(loc = 0.0 , scale = 0.01 , size = 1 + X.shape[1])
        self.w_ = np.zeros(1 + X.shape[1]) 
        self.cost_ = [] 
        for i in range(self.n_iter):
            net_input_matrix = self.net_input(X)
            output_matrix = self.activation(net_input_matrix) 
            errors_matrix = (y - output_matrix)
            self.w_[1:] += self.eta *X.T.dot(errors_matrix)
            self.w_[0] += self.eta*errors.sum()
            cost = (errors**2).sum() / 2.0 
            self.cost_.append(cost) 
            
        return self 
    
    def net_input(self,X):
        '''
        calculate net input
        '''
        return np.dot(X,self.w_[1:]) + self.w_[0] 
    
    
    def activation(self,X):
        '''
        compute linear activation
        '''
        return X
    
    
    def predict(self,X):
        '''
        return class label after unit step
        '''
        return np.where(self.activation(self.net_input(X)) >=0.0 , 1,-1)
        
        
        