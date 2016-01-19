'''
Created on Jan 18, 2016

@author: Krish
'''
from binarySearchTree import binarySearchTree
from treeNode import treeNode
from linkList import Node,LinkedList  
class Z(binarySearchTree):
     def __init__(self):
         super().__init__() 
         
     
     def minimumHeightTree(self,list):
         self._minimumHeightTree(list)
         
     def _minimumHeightTree(self,l):
         #print("Tree till now is"),
         #self.inOrder(self.root)
         if len(l)==1:
             self.put(l[0], l[0])
             return 
         if(len(l)>1):
             self.put(l[len(l)//2],l[len(l)//2])      
             self._minimumHeightTree(l[:len(l)//2])
             self._minimumHeightTree(l[len(l)//2 +1:]) 
             
################################Testing#########################################


myTree = Z()
list=[50,20,100,10,25,80,110,5,11,24,26,70,90,105,120]
for item in list:
    myTree[item]=item   
    
myTree.minimumHeightTree(list)             
myTree.inOrder(myTree.root)