'''
Created on Nov 5, 2015

@author: Krish
'''
class BinHeap:
     def __init__(self):
        self.heaplist=[0]
        self.currentSize=0
        
     def perup(self,i):   
         while i//2>0:
             if(self.heaplist[i//2]>self.heaplist[i]):
                 self.heaplist[i//2],self.heaplist[i]=self.heaplist[i],self.heaplist[i//2] 
             i=i//2
                        
     def insert(self,k):
         self.heaplist.append(k)
         self.currentSize=self.currentSize+1
         self.perUp(self.currentSize)
         
     
     def minchild(self,i):
         if  i*2 + 1> self.currentSize:
             return i*2
         else:  
             if self.heaplist[i*2]<self.heaplist[i*2 + 1]:
                 return i*2
             else:
                 return i*2 +1
         
                
     
     def perdown(self,i):    
         while(i*2<=self.currentSize):
             mc=self.minchild(i)
             if self.heaplist[i]>self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc]=self.heaplist[mc],self.heaplist[i]
                 
             i=mc
     
                  
     def delmin(self):    
         value=self.heaplist[1]
         self.heaplist[1]=self.heaplist[self.currentSize]
         self.currentSize=self.currentSize-1
         self.heaplist.pop()
         self.perdown(1)
         return value
         
     def buildheap(self,alist):  
         #self.heaplist=[0]+ alist[:]  
         i=len(alist)//2
         self.currentSize=len(alist)
         self.heaplist=[0]+ alist[:]
         while(i>0):
             self.perdown(i)
             i=i-1
         return (self.heaplist)

#alist=[54,26,93,17,77,31,44,55,20]
#print("The unsorted list",alist)            
#l=BinHeap()
#bheap=l.buildheap(alist) 
#print("The Binary heap is",bheap)
#print(l)
#x=[]
#for i in range(0,len(alist)):
     #x.append(l.delmin())

#print("The sorted list is" ,x)        