'''
Created on Jan 4, 2016

@author: Krish
Q:Implement myQueue class which implements a queue using two stacks
-point out how it can be make more optimum
'''
import random
from NodeStack import NodeStack
class myQueue:
     def __init__(self):
        self.s1=NodeStack()
        self.s2=NodeStack()
        
     def dequeue(self):
         if(self.s2.isEmpty()):
             print("No element in Queue")
             return -1
         while(not(self.s2.isEmpty())):
             self.s1.push(self.s2.pop())
         x=self.s1.pop()
         while(not(self.s1.isEmpty())):
             self.s2.push(self.s1.pop())  
         return x
     
     def enqueue(self,item):
         self.s2.push(item)
                   
     def isEmpty(self):
         return self.s2.isEmpty()
     
     def show(self):
         print("Printing Queue from 1st element")
         self.s2.show()
                  
#Testing
mq=myQueue()
for  item in [1,24,28,27,12,21,22,10,11,7]:
     mq.enqueue(item)
print("Queue is")
mq.show()
print("Dequeuing")
print(mq.dequeue())
print("Queue is")
mq.show() 
print("Dequeuing")
print(mq.dequeue())
mq.enqueue(1)
print("Queue is")
mq.show() 
print("Dequeuing")
print(mq.dequeue())
print("Queue is")
mq.show()             