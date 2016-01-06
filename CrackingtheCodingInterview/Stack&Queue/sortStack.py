'''
Created on Jan 5, 2016

@author: Krish
Q:Write a program to sort a stack in ascending order(with biggest items on top).
You may use additional stacks to hold items,but you may not copy the elements into any other
data structure(such as an array).The stack supports the following operations:peek, push,pop and isEmpty
-Try to better your algorithm
'''
from NodeStack import NodeStack
import random

class sort(NodeStack):
     def sortStack(self):
         if(s.isEmpty()):
             print("stack is already Empty")
             return -1
         self.f=NodeStack()
         self.i=NodeStack()
         self.f.push(s.pop())
         while(not(s.isEmpty())):
                 while(not(s.isEmpty())):
                     if(s.peek()>self.f.peek()):
                         self.f.push(s.pop())
                     else:
                         break
                 while(not(self.f.isEmpty())):
                     if(s.peek()<self.f.peek()):
                         self.i.push(self.f.pop())
                     else:
                         break
                 if(not(s.isEmpty())):
                     self.f.push(s.pop()) 
                 while(not(self.i.isEmpty())):
                     self.f.push(self.i.pop())
                 #print("s is")
                 #s.show()
                 #print("f is")
                 #self.f.show()
             
         return self.f.show()
 
s=sort()
for item in random.sample(range(30),10):
     s.push(item)
print("original stack is")
s.show()
print("sorted stack is")
s.sortStack()
                        