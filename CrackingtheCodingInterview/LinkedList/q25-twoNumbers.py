'''
Created on Dec 29, 2015

@author: Krish

Q:You have two numbers represented by linked list,where each node contains a single digit.The digits are stored
in reverse order ,such that the 1's digit at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list
-Is External buffer allowed?
-Singly linked list or doubly linked list
'''
from linkList import Node
from linkList import LinkedList

def twoNo(l1,l2):
     
     if(l1==None or l1.size()==0):
         return l2
     
     if(l2==None or l2.size()==0):
         return l1
     
     n1=no(l1)
     print("n1 is",n1)
     
     n2=no(l2)
     print("n2 is",n2)
     n=n1+n2
     n=str(n) 
     print("n is",n)
     l=LinkedList()
     for item in n:
         l.addNode(item)
         
     l.show()    
     return l    
 
def no(l):
     current=l.head
     s=""
     stack=[]
     while(current!=None):
         stack.append(current.getData())
         current=current.getNext()
     
     while(len(stack)!=0):
         s=s+str(stack.pop())    
     
     return int(s)    

l1=LinkedList()
l2=LinkedList()
for item in [6,1,7]:
     l1.addNode(item)
for item in [2,9,5]:
     l2.addNode(item)
     
twoNo(l1, l2)