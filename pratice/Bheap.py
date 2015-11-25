'''
Created on Sep 11, 2015

@author: Krish
'''
class BinHeap:
    
     def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
        
     def percUp(self,i):
         while i // 2 > 0:
             if self.heapList[i] < self.heapList[i // 2]:
                 tmp = self.heapList[i // 2]
                 self.heapList[i // 2] = self.heapList[i]
                 self.heapList[i] = tmp
             i = i // 2
      
      
     def insert(self,k):
         self.heapList.append(k)
         self.currentSize = self.currentSize + 1
         self.percUp(self.currentSize)
                
     def percDown(self,i):
         while (i * 2) <= self.currentSize:
             mc = self.minChild(i)
             if self.heapList[i] > self.heapList[mc]:
                 tmp = self.heapList[i]
                 self.heapList[i] = self.heapList[mc]
                 self.heapList[mc] = tmp
             i = mc

     def minChild(self,i):
         if i * 2 + 1 > self.currentSize:
                 return i * 2
         else:
             if self.heapList[i*2] < self.heapList[i*2+1]:
                 return i * 2
             else:
                 return i * 2 + 1
        
     def delMin(self):
    
         retval = self.heapList[1]
         self.heapList[1] = self.heapList[self.currentSize]
         self.currentSize = self.currentSize - 1
         self.heapList.pop()
         self.percDown(1)
         return retval


     def buildHeap(self,alist):
         #print("here")
         i = len(alist) // 2
         self.currentSize = len(alist)
         self.heapList = [0] + alist[:]
         #print(self.heapList,i) 
         while (i > 0):
             #print("here")
             self.percDown(i)
             i = i - 1  
         
         return (self.heapList)    

alist=[54,26,93,17,77,31,44,55,20]
print("The unsorted list",alist)            
l=BinHeap()
bheap=l.buildHeap(alist) 
print("The Binary heap is",bheap)
#print(l)
x=[]
for i in range(0,len(alist)):
     x.append(l.delMin())

print("The sorted list is" ,x)     