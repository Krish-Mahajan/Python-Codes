'''
Created on Jan 2, 2016

@author: Krish
''' 

from linkList import Node
from linkList import LinkedList  

class NodeQueue:
     def __init__(self,first=None,last=None):
         self.first=first
         self.last=last
      
     def enqueue(self,item):    
         n=Node(item)
         if(self.first==None):
             self.last=n
             self.first=self.last
         else:
             self.last.next=n
             self.last=n    
     
     def dequeue(self):
         if(self.first!=None):
             item=self.first
             self.first=self.first.next
             print("Item dequeued is",item.getData())
             print("New First Element is",self.first.getData())
             return item.getData()  
         print("No item in Queue")
         return None
     
     def show(self):
         print(" First Element of Queue",self.first.getData())
         print("Last Element of Queue is",self.last.getData())
         current=self.first
         while(current!=None):
             print(current.getData()) 
             current=current.next
         
ns=NodeQueue()
for item in [1,2,3,4,5]:
        ns.enqueue(item)
print("Queue is")
ns.show()
print("Dequeuing")
ns.dequeue()
print("Queue is")
ns.show()  
print("Dequeuing")      
ns.dequeue()
ns.dequeue()
print("Enqueqing")
ns.enqueue(10)
ns.enqueue(11)
print("Queue is")
ns.show()        