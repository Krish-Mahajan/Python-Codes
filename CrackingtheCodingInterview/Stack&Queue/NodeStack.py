'''
Created on Jan 2, 2016

@author: Krish
'''
from linkList import Node
#from linkList import LinkedList 

class NodeStack(object):
     def __init__(self):
         self.top=None
         self.size=0    
     def pop(self):
         if(self.top!=None):
             item= self.top
             self.top=self.top.next
             self.size=self.size-1
             #print("Item Popped is",item.getData())
             #print("New top element is",self.top.getData())
             return item.getItem()
         self.size=0
         print("No item in stack")
         return None    
     
     def push(self,item):
         self.size=self.size+1
         n1=Node(item) 
         n1.next=self.top
         self.top=n1
         
     def peek(self):
         return self.top.getItem()    
     
     def showStack(self):
         if(self.top==None):
             print("No element in stack")
             return -1
         current=self.top
         while(current!=None):
             print(current.getItem()) 
             current=current.next
     
     def isEmpty(self):
         return (self.top==None)
     
     def stackSize(self):
         return self.size
 
'''
ns=NodeStack()
for item in [1,2,3,4,5]:
        ns.push(item)
print("Stack is")
ns.show()
print("Popping")
ns.pop()
print("Stack is")
ns.show()  
print("Popping")      
ns.pop()
ns.pop()
print("Pushing")
ns.push(10)
ns.push(11)
print("Stack is")
ns.show()
ns.pop()
print(ns.isEmpty())
ns.pop()
ns.pop()
ns.pop()
print(ns.isEmpty())
ns.show()
'''