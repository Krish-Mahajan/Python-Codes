'''
Created on Sep 8, 2015

@author: Krish
'''
def missingNumber(alist):
     n=len(alist)+1
     print("length of list is ",n)
     Idealsum=(n-1)*((n)/2)
     Actualsum=0
     
     for i in range (0,len(alist)): 
         Actualsum=Actualsum+alist[i]
             
     print("Ideal Sum is",Idealsum)
     print("Acual Sum is",Actualsum)
     return(Idealsum - Actualsum)   
 
alist = [0,5,2,4,3,1]
n=missingNumber(alist)
print("missing_number",n) 