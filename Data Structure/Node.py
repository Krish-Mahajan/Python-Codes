'''
Created on Oct 2, 2015

@author: Krish
''' 


class TreeNode:
     def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
     
     def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn
     
     
     def hasLeftChild(self):
        return self.leftChild

     def hasRightChild(self):
        return self.rightChild

     def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

     def isRightChild(self):
        return self.parent and self.parent.rightChild == self

     def isRoot(self):
        return not self.parent

     def isLeaf(self):
        return not (self.rightChild or self.leftChild)

     def hasAnyChildren(self):
        return self.rightChild or self.leftChild

     def hasBothChildren(self):
        return self.rightChild and self.leftChild

     def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
     
     def inOrderTraversal(self):
        
         if  self:
             #print(self.key)
             #print("Here1")
             if  self.hasLeftChild():
                 #print("here2")
                 #print(type(self.leftChild))
                 #print(self.leftChild.key)
                 for elem in self.leftChild.inOrderTraversal():
                      yield elem
              
             yield self
             
             if  self.hasRightChild():
                 for elem in self.rightChild.inOrderTraversal():
                     yield elem
     