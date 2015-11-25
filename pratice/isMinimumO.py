'''
Created on Jul 10, 2015

@author: Krish
'''
import time
from random import randrange

def findMin(alist):
   overAllMin=alist[0]
   for i in alist:
     isSmallest = True
     for  j in alist:
       if i>j:
        isSmallest=False
        continue
     if isSmallest:
        OverAllmin = i
        
   return OverAllmin
            
print(findMin([5,4,2,1,0]))
print(findMin([0,4,2,1,5]))

       
alist=input("Please enter your list")
alist=list(alist)
print
    