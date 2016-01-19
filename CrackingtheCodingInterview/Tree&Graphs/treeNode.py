'''
Created on Jan 7, 2016

@author: Krish
'''
class treeNode(object):
     def __init__(self,key,value=None,left=None,right=None,parent=None):
         self.key=key
         self.payLoad=value
         self.left=left
         self.right=right
         self.parent=parent
    
     def isRoot(self):
         return (self.parent==None)
     
     def isLeftChild(self):
         return (self.parent  and self.parent.left==self)
     
     def getLeftChild(self):
         return (self.left)
     
     def getRightChild(self):
         return (self.right)
     
     def isRightChild(self):
         return (self.parent and self.parent.right==self)
     
     def hasAnyChild(self):
         return (self.left or self.right)
     
     def hasOneChild(self):
         return ((self.left and not self.right) or (not self.left and self.right))
     
     def hasLeftChild(self):
         return self.left
     
     def hasRightChild(self):
         return self.right
     
     def isLeaf(self):
         return (not(self.left) and not(self.right))
     
     def hasBothChild(self):
         return (self.left and self.right)
     
     def replaceNodeData(self,key,value,left,right,parent):
         self.key=key
         self.payLoad=value
         self.left=left
         self.right=right
         if  self.hasLeftChild():
             self.leftChild.parent=self
         if  self.hasRightChild():
             self.rightChild.parent=self
             
     def __iter__(self):
         if self:
              if self.hasLeftChild():
                     for elem in self.leftChiLd:
                        yield elem
              yield self.key
              if self.hasRightChild():
                     for elem in self.rightChild:
                        yield elem        
         
     def findSuccessor(self):
         succ = None
         if self.hasRightChild():
             succ = self.right.findMin()
         else:
             if self.parent:
                 if self.isLeftChild():
                       succ = self.parent
                 else:
                       self.parent.right = None
                       succ = self.parent.findSuccessor()
                       self.parent.right = self
         return succ   
      
     def findMin(self):
         current = self
         while current.hasLeftChild():
             current = current.left
         return current 
     
     def spliceOut(self):
         if self.isLeaf():
             if self.isLeftChild():
                 self.parent.left = None
             else:
                 self.parent.right = None
         elif self.hasAnyChildren():
             if self.hasLeftChild():
                 if  self.isLeftChild():
                     self.parent.left = self.leftChild
                 else:
                     self.parent.right = self.leftChild
                     self.left.parent = self.parent  
             else:
                 if self.isLeftChild():
                     self.parent.left = self.rightChild
                 else:
                     self.parent.right = self.rightChild
                     self.right.parent = self.parent   
                     
     def getValue(self):
         return self.payLoad                              
     
     def getParent(self):
         if(self.isRoot()):
             return None
         else:
             return self.parent