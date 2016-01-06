'''
Created on Dec 27, 2015

@author: Krish  
Q:Write a code to partition a linked list around a value X,such that all nodes less than x come 
before all nodes greater than or equal to x
-If size of linked list known?
-Double Linked list or single Linked list?
-Are we allowed to used another linklist?
'''
from linkList import LinkedList
from linkList import  Node


def Partition(l,x):
     if(l.search(x)):
         current=l.head
         #index=1
         while(current.getData()!=x):
             current=current.getNext()
             #index=index+1
         print("Current Element is",current.getData())
         #print("Current Element index is",index)
         temp=l.head
         previous=Node()
         previous.setNext(temp)
         tempIndex=1
         
         while(temp!=None):
             print("************")
             print("Previous is",previous.getData())
             print("Temp is",temp.getData())
             #print("current.getNext() is",current.getNext())
             print("************")
             exchange=False
             if(temp.getData()>current.getData()):
                 if(temp==l.head):
                     l.head=temp.getNext()
                 previous.setNext(temp.getNext())
                 temp.setNext(current.getNext())
                 current.setNext(temp)       
                 temp=previous
                 exchange=True
                 #l.show
                 
             if(temp.getData()<current.getData()):
                 previous.setNext(temp.getNext())
                 temp.setNext(l.head)
                 l.head=temp
                 temp=previous
                 exchange=True
             
             
             if(not exchange):
                 previous=previous.getNext()
             temp=previous.getNext()
             
             
             l.show()
     else:
        print("Item Not Present in LinkedList")
        return -1  
       
l=LinkedList()       
for item in [1,1,1,1,0,1,1,1] :
     l.addNode(item)
l.show()

Partition(l,1)