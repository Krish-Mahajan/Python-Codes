'''
Created on Oct 15, 2015

@author: Krish
'''
def fn(n,i):
     if n>1:
       i=i+1  
       print("still going",i)
       i=fn(n//2,i)
       i=fn(n//2,i)  
     return i  
fn(2,0)     