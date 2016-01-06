'''
Created on Jan 3, 2016

@author: Krish
'''
'''
Created on Jan 3, 2016
@author: Krish

Q:Describe how you could use a single array to implement three stacks.
-think of constraint yourself.
-first think static and then dynamic
'''
class ArrayStacks:
     def __init__(self):
         self.stackSize=9
         self.buffer=3*10*[0]
         self.stackPointer=[-1,-1,-1]
     
     def push(self,stackNum,Value):
         if (self.stackPointer[stackNum]>=self.stackSize):
             print("Stack Out of Size")
             return -1
         #print("Stack is",stackNum)
         self.stackPointer[stackNum]=self.stackPointer[stackNum]+1
         self.buffer[self.topOfStack(stackNum)]=Value
             
     def topOfStack(self,stackNum):
         return stackNum*(self.stackSize) + self.stackPointer[stackNum]
         
     def pop(self,stackNum):
         if (self.stackPointer[stackNum]==-1):
             print("Stack Empty")
         #print("Stack is",stackNum)
         value=self.buffer[self.topOfStack(stackNum)-1]
         self.buffer[self.topOfStack(stackNum)-1]=0
         self.stackPointer[stackNum]=self.stackPointer[stackNum]-1
         return value 
     
     def peek(self,stackNum):
         if (self.stackPointer[stackNum]==-1):
             print("Stack Empty")
             return -1
         #print("Stack is",stackNum)
         return self.buffer[self.topOfStack(stackNum)-1]
     
     def isEmpty(self,stackNum):
         return(self.stackPointer[stackNum]==-1)
     
     def show(self,stackNum):
         l=[]
         for i in range(self.stackSize*stackNum,self.stackSize*stackNum+self.stackPointer[stackNum]):
             l.append(self.buffer[i])
         print(l)    

'''
a=ArrayStacks()
for i in range(10):
    a.push(0, i+1)
    a.push(1,i+11)
    a.push(2,i+21)
print(a.stackPointer)

a.show(0)
a.show(1)
a.show(2)
#a.show(2)
a.push(0,21)
a.push(1,21)

print(a.pop(0))
print(a.pop(1))
print(a.peek(0))
print(a.peek(1))

for i in range(9):
    a.pop(0)
    
print(a.isEmpty(0))    
print(a.buffer)
'''