'''
Created on Oct 12, 2015

@author: Krish
'''
def  Csort(alist):
     max=alist[0]
     for i in range(0,len(alist)):
         if  alist[i]>max:
             max=alist[i]
     print("max element is",max)        
         
     c=[0]*(max+1)
     print(c)
     for value in alist:
         c[value]=c[value]+1
     print("c initially is",c) 
       
     for i in range(1,len(c)):
         c[i]=c[i-1]+c[i]
     print("c now is",c)    
         
     sorted_alist=[0]*len(alist)
     for i in reversed(range(0,len(alist))):
         sorted_alist[c[alist[i]]-1]=alist[i] 
         c[alist[i]]=c[alist[i]]-1
         print("sorted list is ",sorted_alist)    
                                           
                                           
alist=[0,3,2,0,1,1,4,10,2,3]
Csort(alist)