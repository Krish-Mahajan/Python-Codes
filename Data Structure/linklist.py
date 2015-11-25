'''
Created on Nov 24, 2015

@author: Krish
'''
import random
class Node(object):
     def __init__(self, data=None, next_node=None):
         self.data = data
         self.next_node = next_node

     def get_data(self):
         return self.data

     def get_next(self):
         return self.next_node

     def set_next(self, new_next):
         self.next_node = new_next

class LinkedList(object):
     def __init__(self, head=None):
         #head=Node(head)
         self.head = head    
        
     def insert(self, data):
         new_node = Node(data)
         new_node.set_next(self.head)
         self.head = new_node       
         
     def size(self):
         current = self.head
         count = 0
         while current:
             count += 1
             current = current.get_next()
         return count
     
     def search(self, data):
         current = self.head
         found = False
         while current and found is False:
             if current.get_data() == data:
                 found = True
             else:
                 current = current.get_next()
         if current is None:
             raise ValueError("Data not in list")
         return current   
 
     def delete(self, data):
         current = self.head
         previous = None
         found = False
         while current and found is False:
             if current.get_data() == data:
                 found = True
             else:
                 previous = current
                 current = current.get_next()
         if current is None:
             raise ValueError("Data not in list")
         if previous is None:
             self.head = current.get_next()
         else:
             previous.set_next(current.get_next()) 
         
     def sortlist(self):
         self.show()
         current=self.head
         previous=Node(None)
         previous.next_node=current
         while(current.next_node!=None):
             print("current is",current.data)
             print("next is",current.next_node.data)
             print("previous",previous.data)
             if(current.next_node.data<current.data):
                 previous.next_node=current.next_node
                 x=current.next_node.next_node
                 current.next_node.next_node=current
                 current.next_node=x
                 previous=previous.next_node
             else:    
                 previous=current    
                 current=current.next_node    
               
            
             self.show()
         return self    
     
     def show(self):
         ll=[]
         current=self.head
         while(current.next_node!=None):
             ll.append(current.data)
             current=current.next_node
         print(ll) 
            
l=LinkedList()        
#random.sample(range(30),10)
#[28, 9, 26, 19, 13, 1, 22, 29, 5]
for item in [28, 9, 26, 19, 13, 1, 22, 29, 5] :
     l.insert(item)

l.sortlist()
