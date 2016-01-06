'''
Created on Jan 3, 2016

@author: Krish


Created on Jan 2, 2016
Q:How would you design a stack which,in addition to push and pop,also has a function min which returns the minimum element?
Push,pop and min should all operate in O(1) time.
-Always do the maths before writing the code
-No constraint on space complexity,so start using it
'''
from linkList import Node
from linkList import LinkedList 
import random
class minStack:
     def __init__(self):
         self.top=None
         self.topMinimum=[]
             
     def pop(self):
         if(self.top!=None):
             item= self.top
             self.top=self.top.next
             #print("Item Popped is",item.getData())
             #print("New top element is",self.top.getData())
             self.topMinimum.pop()
             return item.getData()
         
         print("No item in stack")
         return None    
     
     def push(self,item):
         ## Regular stack
         n1=Node(item) 
         n1.next=self.top
         self.top=n1
         
         ##stack maintaing minimum
         if(self.topMinimum==[]):
             self.topMinimum.append(item)
         else:
             if(item<self.topMinimum[len(self.topMinimum)-1]):
                 self.topMinimum.append(item)
             else:
                 self.topMinimum.append(self.topMinimum[len(self.topMinimum)-1])
         
         
     def peek(self):
         return self.top.getData()    
     
     def show(self):
         print("stack is")
         current=self.top
         while(current!=None):
             print(current.getData()) 
             current=current.next
         print("Minimum order of stack is")
         print(self.topMinimum)  
         
     def minimum(self):
         return self.topMinimum[len(self.topMinimum)-1]
         
ns=minStack()
for item in random.sample(range(30),10):
        ns.push(item)
print("Stack is")
ns.show()

print("minimum is",ns.minimum())

ns.pop()
ns.pop()
ns.pop()
ns.show()
print("minimum is",ns.minimum())
'''
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
'''

