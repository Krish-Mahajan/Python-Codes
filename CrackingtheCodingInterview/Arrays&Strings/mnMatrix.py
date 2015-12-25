'''
Created on Dec 24, 2015

@author: Krish

Q:Write an algorithm such that if an element in an M*N matrix is 0,its entire row and column are set 0

'''
from copy import deepcopy
def mnMatrix(l):
     m1=1
     n1=1
     ll=deepcopy(l)
     def setZero(m1,n1):     
         for i in range(len(ll[m1-1])): ##Setting Row 0
             ll[m1-1][i]=0
             
         for i in range(len(ll)): ##Setting Column 0
             ll[i][n1-1]=0
         
     if(len(l)==0 or l=="None"):
         print("No Matrix")    
     for i in range(len(l)):
         n1=1
         for j in range(len(l[i])):
             #print(l[i][j])
             if (l[i][j]==0):
                 #print(m1,n1)
                 setZero(m1,n1)
                 #print(l)
             n1=n1+1
         m1=m1+1  
     
     
     return ll
 
print(mnMatrix([[1,2,3],[4,5,6],[0,8,9],[10,11,0]]))  