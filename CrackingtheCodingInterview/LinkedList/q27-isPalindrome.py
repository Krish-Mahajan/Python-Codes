'''
Created on Dec 27, 2015

@author: Krish  
Q:Implement a function to check if a list is palindrome?
-Size known or unknown?
-Use of stack allowed or not
-Doubly link list or singly
'''

from linkList import LinkedList
from linkList import  Node
def isPalindrome(l):
     fast=l.head
     slow=l.head
     stack=[]
     while(fast!=None and fast.getNext()!=None): #Even Elements
         stack.append(slow.getData())
         slow=slow.getNext()
         fast=fast.getNext().getNext()
    
     if(fast!=None): #odd Elements
         slow=slow.getNext()
     
     while(slow!=None):
         if(slow.getData()!=stack.pop()):
             return  False
         slow=slow.getNext()
     return True        
 
l=LinkedList()       
for item in "123321" :
     l.addNode(item)

print(isPalindrome(l))