'''
Created on Jan 8, 2016

@author: Krish
'''
import random
class BinaryHeap(object):
     def __init__(self):
          self.heapList=[0] ##DummyElement
          self.heapSize=0
          
     def insert(self,key):
         self.heapList.append(key) 
         self.heapSize=self.heapSize+1
         self.minHeapify(self.heapSize)    
         
     def minHeapify(self,i):
         while (i//2)>0:
             if(self.heapList[i]<self.heapList[i//2]):
                 self.heapList[i//2],self.heapList[i]=self.heapList[i],self.heapList[i//2] 
             i=i//2
             
     
     def deleteMin(self):
         x=self.heapList[1]
         self.heapList[1]=self.heapList[self.heapSize]
         self.heapList.pop()
         self.heapSize=self.heapSize-1
         self._delete(1)
         return x
     
     def _delete(self,i):
         while(2*i<= self.heapSize):
             mc=self.minChild(i)
             if(self.heapList[mc]<self.heapList[i]):
                 self.heapList[mc],self.heapList[i]=self.heapList[i],self.heapList[mc] 
             i=mc
                       
     def minChild(self,i):
         if(2*i+1>self.heapSize):
             return 2*i
         else:
             if(self.heapList[2*i]<=self.heapList[2*i+1]):
                 return 2*i 
             else:
                 return 2*i+1
                   
     def buildHeap(self,alist):
         self.heapSize=len(alist)
         self.heapList=[0] + alist[:]
         i=len(alist)//2
         while(i>0):
             self._delete(i)
             i=i-1
     
     def showHeap(self):
         print(self.heapList)        
                        
l=[]
for item in [0, 1, 2, 12, 18, 3, 29, 21, 26, 22, 23, 14]:
     l.append(item) 

print("Initial list is")
print(l)
print("Heap is")

bh=BinaryHeap()
bh.buildHeap(l)
bh.showHeap()
bh.insert(-1)     
bh.showHeap()    