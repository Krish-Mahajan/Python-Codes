'''
Created on Oct 10, 2015

@author: Krish
'''
def factorial(n):
     if(n==1):
         return n
     
     else:
         return n*factorial(n-1)
     
     
x=factorial(6)
print(x) 
     