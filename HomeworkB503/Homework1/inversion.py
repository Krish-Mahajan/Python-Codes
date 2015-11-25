'''
Created on Sep 8, 2015

@author: Krish
'''
def inversion(alist):
     count=0
     print("following are the inversion pairs:")
     for i in range (0,len(alist)):
         j=i+1
         while j<len(alist):
             if(i<j and alist[i]>alist[j]):
                 count=count+1
                 print("i is",i,",j is ",j,",A[i] is ",alist[i],",A[j] is",alist[j])
                 
             j=j+1    
     print("Total no of inversions are",count)
alist=[6,5,4,3,2,1]
inversion(alist)