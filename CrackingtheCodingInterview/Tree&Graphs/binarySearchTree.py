'''
Created on Jan 7, 2016

@author: Krish
'''
from treeNode import treeNode
from linkList import Node,LinkedList
import random
import sys

class binarySearchTree(object):
     def __init__(self):
          self.root = None
          self.size=0
     
     def length(self):
         return self.size
     
     def getRootValue(self):
         return self.root.payLoad
     
     def getRoot(self):
         return self.root

########################Insertion###############################################     
     def put(self,key,value):
         self.size=self.size+1
         if(not self.root):
             n=treeNode(key=key,value=value)
             self.root=n
         else:
             currentNode=self.root
             self._put(currentNode,key,value)
             
     
     def _put(self,cn,key,value):
         if(cn.key<key):
             if(cn.hasRightChild()):
                 cn=cn.right
                 self._put(cn, key, value)
             else:
                 cn.right=treeNode(key=key,value=value,parent=cn)
         else:
             if(cn.hasLeftChild()):
                 cn=cn.left
                 self._put(cn,key,value)      
             else:
                 cn.left=treeNode(key=key,value=value,parent=cn)
     
     def __setitem__(self,key,value):
         self.put(key, value)  

##########################Traversal#############################################       
     def inOrder(self,node):
         if(node!=None):
             self.inOrder(node.getLeftChild())
             print(node.payLoad)
             self.inOrder(node.getRightChild())
             
     def preOrder(self,node):
         if(node!=None):
             print(node.payLoad)
             self.inOrder(node.getLeftChild())
             self.inOrder(node.getRightChild())
                         
     def postOrder(self,node):   
         if(node!=None):
             self.inOrder(node.getLeftChild())
             self.inOrder(node.getRightChild())
             print(node.payLoad)
             
###############################Search in Tree##################################     
         
     def get(self,key):
         if(self.root):
             res=self._get(key,self.root)
             #print(res.payLoad)
             if(res):
                 #print(res.parent.payLoad)
                 return res
             else:
                 print("Key not in the Tree")
                 return None
         else:
             print("Tree is Empty")
             return None
     
     def _get(self,key,currentNode):
         #print(currentNode.payLoad)
         
         if(not currentNode):
             return None
         
         elif(currentNode.key==key):
             return currentNode
         
         elif(currentNode.key>key):
             return self._get(key, currentNode.left)
         
         else:
             return self._get(key, currentNode.right)   
          
         
     
     def __contains__(self,key):
         if(self._get(key, self.root)):  
             return True
         else:
             return False        
     
     def __getitem__(self,key):
             return self.get(key)   
         
######################Deletion#################################################

     def  delete(self,key):
         if(self.size)>1:
             nodeToRemove=self._get(key,self.root)
             #print(nodeToRemove.payLoad)
             #print(nodeToRemove.parent.payLoad)
             if(nodeToRemove):
                 self._remove(nodeToRemove)
                 self.size=self.size-1
             else:
                 print("Key not in Tree")
                 return -1
         elif self.size==1 and self.root.key==key:
             self.root=None
             self.size=0
         
         else:
             print("Empty Tree")
             return -1
                
     def  _remove(self,nodeToRemove):
        
         ##Case 1 node to be deleted has no children i,e (its a leaf)
         if nodeToRemove.isLeaf():
             if nodeToRemove.isLeftChild():
                 nodeToRemove.parent.left=None
             
             else:
                 #print(nodeToRemove.payLoad)
                 #print(nodeToRemove.parent.payLoad)
                 nodeToRemove.parent.right=None                
         
         ##Case 2 node to be deleted has 1 children   
         elif nodeToRemove.hasOneChild():
             if nodeToRemove.isLeftChild():
                 if nodeToRemove.hasLeftChild():
                     nodeToRemove.left.parent=nodeToRemove.parent
                     nodeToRemove.parent.left=nodeToRemove.left
                 else:
                     nodeToRemove.right.parent=nodeToRemove.parent
                     nodeToRemove.parent.left=nodeToRemove.right
             else:
                 if nodeToRemove.hasLeftChild():
                     nodeToRemove.left.parent=nodeToRemove.parent
                     nodeToRemove.parent.right=nodeToRemove.left
                 else:
                     nodeToRemove.right.parent=nodeToRemove.parent
                     nodeToRemove.parent.right=nodeToRemove.right
                                
         ##Case 3 nodeToRemove Both child
         elif nodeToRemove.hasBothChild(): #interior
             currentNode=nodeToRemove
             succ = currentNode.findSuccessor()
             succ.spliceOut()
             currentNode.key = succ.key
             currentNode.payLoad = succ.payLoad                       
                     
       
######################TestTing################################################# 
                          



'''
print("Tree is") 
myTree.inOrder(myTree.root)
'''

'''
print("Generating Linklist at each depth")
myTree.treeLinkList(myTree.getRoot())
'''

#print(myTree.isBalanced(myTree.getRoot()))
'''
l=[]
for  item in [24, 11, 7, 28, 22, 27, 21, 25, 3, 0]:
     l.append(item)
     myTree[item]=item
print("Keys are")
print(l)
'''

#print("Tree is") 
#myTree.inOrder(myTree.root)
#mytree.postOrder(mytree.getRoot())
#print(myTree.getRootValue())
#print(myTree.get(11))
'''
for item in [17, 29, 27, 26, 16, 11, 0, 5, 1, 14]:
    print(myTree[item])
    print(item in myTree)
'''   
#myTree.delete(17)
#print("Tree after deletion  is") 
#myTree.inOrder(myTree.root)

'''
print("checking if tree is balanced or not")
print(myTree.isBalanced(myTree.getRoot()))
'''
