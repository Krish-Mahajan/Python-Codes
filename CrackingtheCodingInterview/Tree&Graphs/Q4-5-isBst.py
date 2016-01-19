'''
Created on Jan 18, 2016

@author: Krish
'''
from binarySearchTree import binarySearchTree
class X(binarySearchTree):
     def __init__(self):
         super().__init__()
          
     def isBst(self,Node,min,max):
         
         if(Node==None):
             return True
         #print(Node.getValue(),min,max)
         if(Node.getValue()<=min and Node.getValue()>max):
             return False 
         
         if ( not self.isBst(Node.getLeftChild(),min,Node.getValue())): 
             return False
         if  (not self.isBst(Node.getRightChild(),Node.getValue(),max)):
             return False
         
         return True 
     

#################################Testing#######################################
myTree = X()
list=[50,20,100,10,25,80,110,5,11,24,26,70,90,105,120]
for item in list:
    myTree[item]=item
print(myTree.isBst(myTree.getRoot(),-100,1000))       
     
         