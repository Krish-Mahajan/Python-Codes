'''
Created on Jan 18, 2016

@author: Krish
'''
from binarySearchTree import binarySearchTree
class TreeSubset(binarySearchTree):
     def __init__(self):
          super().__init__()
          
     def isSubset(self,tree1,tree2):
         if(not tree1.getRoot()):
             print("Tree 1 is empty")
             return True
         else:
             searchedNode= tree1.get(tree2.getRoot().getValue()) 
             #print("searchedNode is",searchedNode.getValue())
             if(searchedNode==None):
                 print("Tree 2 could not be found ")
                 return False  
             else:
                 return self.treeMatch(searchedNode,tree2.getRoot())
                 
     def treeMatch(self,tree1Node,tree2Node):
         
         if(tree1Node==None and tree2Node==None):
             return True
         print("tree1Node is",tree1Node.getValue(),"tree2Node",tree2Node.getValue())
         if(tree1Node==None or tree2Node==None):
             return False
         
         if(tree1Node.getValue() !=tree2Node.getValue()):
             return False
         
         else:
             return (self.treeMatch(tree1Node.getLeftChild(),tree2Node.getLeftChild()) and 
                     self.treeMatch(tree1Node.getRightChild(),tree2Node.getRightChild()))

##########################Testing###############################################

myTree1 = binarySearchTree()
myTree2 = binarySearchTree()
list1=[50,20,100,10,25,80,110,5,11,24,26,70,90,105,120]
for item in list1:
    myTree1[item]=item           
list2=[100,80,110,70,90,105,121]
for item in list2:
    myTree2[item]=item
check = TreeSubset()
print(check.isSubset(myTree1, myTree2))     