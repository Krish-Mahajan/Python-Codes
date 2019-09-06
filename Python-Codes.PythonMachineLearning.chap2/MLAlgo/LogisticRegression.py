'''
Created on Aug 30, 2019

@author: krish.mahajan@ibm.com
'''
import numpy as np 
class LogisticRegressionGD(object):
    '''
    Adaptive Linear Neuron Classifier 
    
    Parameters 
    ---------
    eta : float 
        Learning rate (between 0.0 and 1.0) 
    n_iter : int 
        passes over the training dataset.
        
    shuffle : bool (default : True) 
        shuffle training data every epoch if True to prevent cycles
    random_state : int 
        Random number generator seed for random weight initialization
        
    Attributes
    ---------- 
    w_ : 1d-array 
        weights after fitting
    cost_ : list 
        sum of squares cost function value averaged over all training samples in each epoch 
    
    '''


    def __init__(self,eta =0.01 , n_iter = 50,random_state = 1 , shuffle = True):
        self.eta = eta 
        self.n_iter = n_iter 
        self.random_state = random_state 
        self.w_initialized = False
        self.shuffle = shuffle
        
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
        
        self._initialize_weights(X.shape[1])  
        self.cost_ = []  
        
        if self.shuffle:
            X ,y = self._shuffle(X,y)
        
        self.cost_
        
        for i in range(self.n_iter): 
            net_input_matrix = self.net_input(X)
            output_matrix = self.activation(net_input_matrix) 
            errors_matrix = y - output_matrix
            self.w_[1:] += self.eta*X.T.dot(errors_matrix)
            self.w_[0] += self.eta*errors_matrix.sum() 
            cost = (-y.dot(np.log(output_matrix)) - (1 -y).dot(np.log(1 -output_matrix)))
            self.cost_.append(cost)


        return self
            
    
    
    def _initialize_weights(self,m):
        ''' Initialize weights to small random numbers'''
        rgen = np.random.RandomState(self.random_state) 
        self.w_ = rgen.normal(loc = 0.0 , scale = 0.01 , size = 1 + m)
        self.w_initialized = True 
        
        
    def _shuffle(self,X,y):
        '''
        shuffling traning data
        '''
        r = np.random.permutation(len(y))
        return X[r],y[r]
        
    
    def net_input(self,X):
        '''
        calculate net input
        '''
        return np.dot(X,self.w_[1:]) + self.w_[0] 
    
    
    def activation(self,z):
        '''
        compute sigmoid activation
        '''
        return 1 / 1 + np.exp(-np.clip(z,-250,250))
    
    
    def predict(self,X):
        '''
        return class label after unit step
        '''
        return np.where(self.activation(self.net_input(X)) >=0.0 , 1,-1)
        
        
   