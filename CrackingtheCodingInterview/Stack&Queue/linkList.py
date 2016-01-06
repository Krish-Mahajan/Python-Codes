'''
Created on Dec 26, 2015

@author: Krish

Data Structure LinkList implementation
'''
class Node(object):
     def __init__(self,item=None,next=None):
         self.item=item
         self.next=next
         
     def getItem(self):
         return self.item
     
     def setItem(self,item):
         self.item=item
         
     def getNext(self):
         return self.next
     
     def setNext(self,newNext):
         self.next=newNext

class LinkedList(object) :
     def __init__(self,head=None):
         
         self.head=head
         
     def isEmpty(self):
         return self.head==None
     
     def addNode(self,item):
         temp=Node(item)
         temp.setNext(self.head)
         self.head=temp
         
     def size(self):
         current=self.head
         
         count=0
         while current!=None:
             current=current.getNext()
             count=count+1
         
         return count    
     
     def search(self,item):
         current=self.head
         found=False
         while (current!=None and not found):
             if(current.getItem()==item):
                 found=True
             else:
                 current=current.getNext()
         return found
     
     def remove(self,item):
  
             current=self.head
             previous=None
             found=False
             while (current!=None and not found):
                 if(current.getItem()==item):
                     found=True
                 else:
                     previous=current
                     current=current.getNext()
             
             if previous==None:
                 self.head(current.getNext())
                 
             else:
                 previous.setNext(current.getNext())
         
     def show(self):
         ll=[]
         #print("First Element is",self.first.data)
         #print("Head Element is",self.head.data)
         #print("Next element of head is",self.head.next_node.data)
         current=self.head
         while(current!=None):
             ll.append(current.getItem())
             #print(current.getData())
             current=current.getNext()
                
         print(ll[::1])    
'''
l=LinkedList()       
#random.sample(range(30),10)
#[28, 9, 26, 19, 13, 1, 22, 29, 5]
for item in [28, 9, 26, 19, 13, 1, 22, 29, 5] :
     l.addNode(item)
l.show()
for item in [28, 9, 26, 19, 13, 1, 22, 29, 5] :
     print(l.search(item))

print(l.size())

for item in [28, 9, 26, 19, 13, 1, 22, 29, 5] :
     l.remove(item)     
     l.show()                          
'''                                 
             