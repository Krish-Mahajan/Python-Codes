'''
Created on Jan 5, 2016

@author: Krish
Q:Imagine a (literal) stack of plates...etc
-Use of multiclasses (Node,stack,setOfstacks)
'''
from NodeStack import NodeStack
class setOfStacks(object):
     def __init__(self):
         self.ss=NodeStack()
         
         
     
     def push(self,item):
         if(self.ss.isEmpty()):
             s=NodeStack()
             s.push(item)
             self.ss.push(s)
         else:
             if(self.ss.peek().stackSize()<3):
                 #print(type(self.ss.peek()))
                 self.ss.peek().push(item)    
             else:
                 s=NodeStack()  
                 s.push(item) 
                 self.ss.push(s) 
     
     def pop(self):            
         if(not(self.ss.isEmpty())):
             if(self.ss.peek().stackSize()!=0):
                 self.ss.peek().pop()
                 if(self.ss.peek().stackSize()==0):
                     self.ss.pop()
             else:
                 
                 self.ss.pop()
                 self.ss.peek().pop()    
             
         else:
             print("No platess in Tray") 
             return -1   
         
     def showSetOfStacks(self):
         if(self.ss.peek().stackSize()==0):
             print("No platesss in Tray") 
             return -1 
         else:
             
             currentStack=self.ss.top
             print(type(currentStack.getItem()))
             #print(self.ss.top)
             #print(type(self.ss.top))
             i=0
             while(currentStack!=None):
                 i=i+1
                 print("Stack",i,"is")
                 currentStack.getItem().showStack()
                 currentStack=currentStack.next

ss=setOfStacks()
for item in [1,2,3,4,5,6,7,8,9]:
     ss.push(item)
print("Plate looks like")  
#ss.showSetOfStacks()  
ss.pop()
ss.pop()
ss.pop()
ss.showSetOfStacks() 
    
             
