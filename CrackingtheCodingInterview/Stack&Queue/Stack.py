'''
Created on Jan 2, 2016

@author: Krish
'''
class stack:
     def __init__(self):
         self.items=[]
        
     def isEmpty(self):
         return self.items==[]
     
     def push(self,item):
         self.items.append(item)
     
     def pop(self,item):
         self.items.pop()
     
     def peek(self):
         return self.items[len(self.items)-1]           
     
     def size(self):
         return len(self.items)