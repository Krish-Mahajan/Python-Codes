'''
Created on Dec 27, 2015

@author: Krish

Q:Given a linklist ,remove duplicates from it.
'''
from linkList import LinkedList
from linkList import Node
import random
def removeDuplicate(l):
     print("Original Linked list")
     l.show()
     l= iSort(l)
     print("Final Sorted Linked List is")
     l.show()
     current=l.head
     previous=Node()
     previous.setNext(current)
     while(current.getNext()!=None):
         print("Current is",current.getData())
         print("Previous is",previous.getData())
         if(current.getData()==current.getNext().getData()):
             while(current.getData()==current.getNext().getData()):
                 current=current.getNext()
             previous.setNext(current)
         previous=current
         current=current.getNext()    
         l.show()    
    
def  iSort(l): 
     current=l.head.getNext()
     previous=l.head
     previous.setNext(current)
     
     while(current!=None):
         exchange=False
         tempCurrent=l.head
         tempPrevious=Node()  
         tempPrevious.setNext(tempCurrent)
         #print("******************************")  
         #print("Current is",current.getData())
         #print("Previous is",previous.getData())
         
         while(tempCurrent!=current and (not exchange)):
             #print("tempCurrent is",tempCurrent.getData())
             #print("tempPrevious is",tempPrevious.getData())
             
             if (tempCurrent.getData()>current.getData()):
                 if(tempCurrent==l.head):
                     previous.setNext(current.getNext())
                     current.setNext(tempCurrent)
                     tempPrevious.setNext(current)
                     l.head=current
                     previous=current
                     current=current.getNext()
                     exchange=True
                     break
                 
                 previous.setNext(current.getNext())
                 current.setNext(tempCurrent)
                 tempPrevious.setNext(current)
                 current=previous.getNext()
                 exchange=True
                 break
             
             tempCurrent=tempCurrent.getNext()
             tempPrevious=tempPrevious.getNext()
         if(not exchange):
             current=current.getNext()
             previous=previous.getNext()
         
         #l.show()    
     return l            
 
l=LinkedList()
for item in [1,2,54,6,2,1,6,-40,6,6,6,0,-13.5,90,0.5,0.5]:
    l.addNode(item)

removeDuplicate(l)