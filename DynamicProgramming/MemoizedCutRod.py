'''
Created on Oct 7, 2015

@author: Krish
'''
def cutRod(p,n,s):
     maxRevenue=p[n] #As per table
     if n==0:
         return 0
     elif s[n]>0:
         return s[n]
     for i in range(1,n):
         #print("n is",n,",i is",i)
         q=p[i]+cutRod(p, n-i,s) 
         #print("q is",q,",n is",n)
         if maxRevenue<q: 
             maxRevenue=q
         s[n]=maxRevenue    
     print(s)    
     return maxRevenue    
 

p=[0,1,5,8,9,10,17,17,20,24,30]
s=[0]*len(p)
n=9
x=cutRod(p,n,s)
print("Max Revenue we can generate by cutting rod of",n," inches is",x)