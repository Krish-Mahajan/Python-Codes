'''
Created on Jan 18, 2016

@author: Krish
'''
from binarySearchTree import binarySearchTree
from treeNode import treeNode
from linkList import Node,LinkedList

class Y(binarySearchTree):
     def __init__(self):
          super().__init__()
          
     def treeLinkList(self,root):  #Assuming Complete Binary Tree
         if(root==None):
             print("Tree is Empty")
             return
         
         l=[] #to store all linklist at every depth
         self._treeLinkList(root,l) #Main Method
         if(len(l)>0):  #Print all the linklist at all the depth
             i=0
             for item in l:
                 i=i+1
                 print("Depth",i)
                 current=item.head
                 while(current!=None):
                     print(current.getData().getValue())
                     current=current.next
                 
         
         
     def _treeLinkList(self,Node,l):
         
         if(len(l)==0):
             ll=LinkedList()
             if(Node.getLeftChild()):
                 ll.addNode(Node.getLeftChild())
                 lChild=True
             else:
                 print("End of Tree:No more left Child")
                 lChild=False
                 return
             if(Node.getRightChild()):
                 ll.addNode(Node.getRightChild())
                 rChild=True
             else:    
                 print("End of Tree:No more right Child")
                 rChild=False
                 return
             l.append(ll)
             if(lChild):
                 Node=Node.getLeftChild()
                 self._treeLinkList(Node, l)
         
         if(len(l)>0):
             ll=LinkedList()
             self.completeTreeLL(l,ll,Node)
             if(Node.getLeftChild()):
                 Node=Node.getLeftChild()
                 self._treeLinkList(Node, l)
         
                 
     
     def completeTreeLL(self,l,ll,Node):
         current=l[-1].head   
         #print("Here")
         #print(current.getData().getValue())
         i=0
         while(current!=None):
             #print(current.getData().getValue())
             if(current.getData().getRightChild()):    
                 #print(current.getData().getRightChild().getValue())
                 ll.addNode(current.getData().getRightChild())
             
             if(current.getData().getLeftChild()):
                 #print(current.getData().getLeftChild().getValue())
                 ll.addNode(current.getData().getLeftChild())
             #print(current.next.getData().getValue())
             #print(current.next.getData().getRightChild().getValue())
             #print(current.next.getData().getLeftChild().getValue())
             current=current.next    
             #print(current.getData().getValue())   
             #print(current.getData().getRightChild().getValue())  
             #print(current.getData().getLeftChild().getValue())
         l.append(ll)  
         
###########################Testing#############################################

myTree = Y()
list=[50,20,100,10,25,80,110,5,11,24,26,70,90,105,120]
for item in list:
    myTree[item]=item
print("Generating Linklist at each depth")
myTree.treeLinkList(myTree.getRoot())
