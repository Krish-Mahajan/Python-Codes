'''
Created on Dec 26, 2015

@author: Krish  

Q: Implement an algorithm to find the kth to last element of a singly linked list
-What is K (distance from last or first element?)
-size of linklist is known(Always ask if its a question of linkList) #Assume its not for non trivial solns
-single linked list or doubly linkList(Always ask if question of linkList)
'''
from linkList import LinkedList 
from linkList import Node

def kthtoLast(l,k): ## If size if known (non recursive solution)
     n=l.size()
     if(k>n):
         print("invalid k")
         return -1
     
     nl=LinkedList()
     count=1
     current=l.head
     while(count<=n-k+1 and current !=None):
         print(current.getData())
         nl.addNode(current.getData())
         current=current.getNext()
         count=count+1
     
     return nl   
 
def kthtolastR(l,k): #Using recursion assuming size is unknown
     if(l==None):
         return 0
     i=kthtolastR(l.getNext(), k)+1
     if(i>=k):
         print(l.getData())
     return i    
l=LinkedList()       
#random.sample(range(30),10)
#[28, 9, 26, 19, 13, 1, 22, 29, 5]
for item in [1,2,3,4,5,6,7] :
     l.addNode(item)
l.show()
print("Using Recursion")
nl=kthtolastR(l.head, 2) 