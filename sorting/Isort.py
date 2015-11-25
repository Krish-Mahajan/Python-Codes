'''
Created on Aug 28, 2015

@author: Krish
'''
def isort(alist):
  for index in range(1,len(alist)):
    print("Current element is : %d" %alist[index] )
    print(alist)
    position=index
    currentValue=alist[position]
    
    while position>0 and alist[position-1]>alist[position]:
     alist[position]=alist[position-1]
     alist[position-1]=currentValue
     position=position-1
     print(alist)
'''
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

alist[position]=currentvalue
'''

def isort2(alist):
     print("Unsorted list is",alist)
     for i in range(1,len(alist)):
         j=i-1
         while j>=0:
             if alist[j]>alist[i]:
                 alist[j],alist[i]=alist[i],alist[j]
                 i=j
                 j=j-1
         print(alist)           
     
alist = [10,9,8,7,6,5,4,3,2,1]
isort2(alist)
#print(alist)
