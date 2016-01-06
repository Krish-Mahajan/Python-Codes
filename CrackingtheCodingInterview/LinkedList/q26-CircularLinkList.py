'''
Created on Dec 29, 2015

@author: Krish
Q:Check if a linklist has a loop?
-is External Buffer allowd?
-singly or doubly linklist

'''
from linkList import Node
from linkList import LinkedList

def  iscircularLinkedlist(l):
     if(l==None):
         return -1
     d={}
     current=l.head
     isCircularList=False
     while(current!=None):
         #print(current.getData())
         if(current.getData() in d):
             isCircularList=True
             return current.getData()
         else:
             d[current.getData()]=1
         current=current.getNext()
     
     return isCircularList
 
l=LinkedList()

for item in ["C","E","D","C","B","A"]:
    l.addNode(item)
l.show()
print(iscircularLinkedlist(l))
