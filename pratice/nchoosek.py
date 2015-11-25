'''
Created on Sep 1, 2015

@author: Krish
'''
def subset(n, k): 
    if k == 0:
        return 1
    if n == k:
        return 1
    else:
        return subset(n-1, k-1) + subset(n-1, k)
    
print(subset(4,2))