'''
Created on Oct 10, 2015

@author: Krish
'''
def listReverse(l):
     rl=[]
     return Reverse(l,rl)
     
def Reverse(l,rl):  
     print("list is ",l)
     if len(l)==1:
         return rl.append((l[0]))
     else:
         rl.append(l[len(l)-1])
         print("Reverse list is",rl)
         Reverse(l[0:len(l)-1],rl)
         return rl
         
         
         
     
l=[4,3,2,7,8]

print(listReverse(l))     
