'''
Created on Sep 7, 2015

@author: Krish
'''
def unknown(alist):
     for i in range(0,len(alist)):
         #print("The current element is",alist[i])
         #print("List is",alist)
         if(alist[i]>alist[len(alist)-1]):
             alist[i],alist[len(alist)-1]=alist[len(alist)-1],alist[i]
         #print(alist)
     #return(alist[len(alist-1)])        
 
 
alist = [31,41,100,26,41,58]
n=unknown(alist)
print(n)