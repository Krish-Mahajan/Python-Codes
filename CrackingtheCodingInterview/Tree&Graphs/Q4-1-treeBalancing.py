'''
Created on Jan 18, 2016

@author: Krish
'''
from binarySearchTree import binarySearchTree
class W(binarySearchTree):
         def __init__(self):
             super().__init__()
        
         def isBalanced(self,Node):
             
             if  Node==None:    ##Base Case
                 return True  
             
             else:
                 lh=self._getHeight(Node.left)
                 rh=self._getHeight(Node.right)
                 #print("Node is",Node.getValue())
                 #print("Left & Right Heights are",lh,rh)
                 if( abs(lh-rh)>1):
                     return False
                 
                 else:
                     return (self.isBalanced(Node.left) and self.isBalanced(Node.right))
         
         def _getHeight(self,node):  
             if(node==None): ##Base Case
                 return 0
             else:
                 return max(self._getHeight(node.left),self._getHeight(node.right))+1  
                    
myTree = W()
list=[50,20,100,10,25,80,110,5,11,24,26,70,90,105,120]
for item in list:
    myTree[item]=item           

print(myTree.isBalanced(myTree.getRoot()))           