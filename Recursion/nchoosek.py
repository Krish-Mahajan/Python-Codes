'''
Created on Oct 10, 2015

@author: Krish
'''
def nchoosek(n, k): 
     if k == 0:
        return 1
     if n == k:
        return 1
     else:
        return nchoosek(n-1, k-1) + nchoosek(n-1, k)
    
print(nchoosek(10,2))