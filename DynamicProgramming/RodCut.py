'''
Created on Oct 7, 2015

@author: Krish
'''


def cutRod(p,n):
     maxRevenue=p[n] #As per table
     if n==0:
         return 0
     for i in range(1,n):
         #print("n is",n,",i is",i)
         q=p[i]+cutRod(p, n-i) 
         #print("q is",q,",n is",n)
         if maxRevenue<q: 
             maxRevenue=q
     return maxRevenue    
 
p=[0,1,5,8,9,10,17,17,20,24,30]
x=cutRod(p,9)
print("Max Revenue we can generate by cutting rod of 9 inches is",x)