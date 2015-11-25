'''
Created on Sep 4, 2015

@author: Krish
'''
def bubblesort1(alist):
     print("The initial list is ",alist)
     s=len(alist)
     for i in range(1,len(alist)):
         j=1
         #print("j is " ,j)
         while j<s:
             if alist[j-1]>alist[j]:
                 #print("here")
                 alist[j],alist[j-1]=alist[j-1],alist[j]
             j=j+1
         s=s-1
         print(alist)
               

#print(alist)

def bubblesort2(alist):
     print("Unsorted list is",alist)
     for i in reversed(range(0,len(alist))):
         for j in range(0,i):
             if alist[j]>alist[j+1]:
               alist[j],alist[j+1]=alist[j+1],alist[j]   
         print(alist)
         
         
alist = [10,9,8,7,6,5,4,3,2,1]
bubblesort2(alist)         