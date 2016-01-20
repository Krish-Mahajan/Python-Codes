'''
Created on Jan 20, 2016

@author: Krish
'''
from binarySearchTree import binarySearchTree
class K(binarySearchTree):
     def __init__(self,allPath=None,valueToMatch=None):
         super().__init__()
         self.allPath=[]
         self.valueToMatch=None
     
     def path(self,node,value):
         self.valueToMatch=value
         if(node==None):
             return
         else:
             self._paths(node, value)
             self.path(node.getLeftChild(),value)
             self.path(node.getRightChild(),value) 
             
     def _paths(self,node,value):
         
         if (node==None):
             return
         
         if (node.getValue()==value):
             self.storePath(node)
         
         else:
             #print("Node is",node.getValue(),"value is",value)
             self._paths(node.getLeftChild(), value-node.getValue())
             self._paths(node.getRightChild(), value-node.getValue()) 
         
                       
     def storePath(self,node):
         #print(self.allPath)
         x=self.valueToMatch
         path=[]
         while(x!=0):
             path.append(node.getValue())
             x=x-node.getValue()
             node=node.getParent()
         print("Latest path is",path)
         self.allPath.append(path)
         print("All path till now is",self.allPath)
                 
            
 
myTree = K()
list=[50,20,100,10,25,80,110,5,11,40,26,55,90,105,120]
for item in list:
    myTree[item]=item  
    
myTree.path(myTree.getRoot(), 21+20)         