'''
Created on Jan 18, 2016

@author: Krish
'''
from binarySearchTree import binarySearchTree
class CommonAncestor(binarySearchTree):
     def __init__(self):
          super().__init__()
          
     def commonAncestor(self,node1,node2):
         if(node1.getValue()==node2.getValue()):
             return Node1.getValue()
         
         elif(not node1.isRoot()):
             current=node1.getParent()
             while(current !=None):
                 x=self._get(node2.getValue(),current)
                 if(x):
                     return current.getValue()
                 current=current.getParent()
         
         elif(node1.isRoot() or node2.isRoot()):
             print("One of the Node is root")
             return        

############################Testing############################################                 
myTree = CommonAncestor()
list=[50,20,100,10,25,80,110,5,11,24,26,70,90,105,120]
for item in list:
    myTree[item]=item
print(myTree.commonAncestor(myTree.get(11), myTree.get(105)))                  