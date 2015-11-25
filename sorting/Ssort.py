'''
Created on Sep 4, 2015

@author: Krish
'''
def ssort(alist):
     print("In ssort, the initial list is ",alist)
     s=len(alist)
     for i in range(0,len(alist)):
         print("In for the list is ",alist)
         a=0
         j=0
         k=0
         currentValue=alist[j]
         #print("The current value is ",alist[j])
         while j<s-1:
             a=0
             #currentValue=alist[j]
             print("The current value is ",currentValue)
             if currentValue > alist[j+1]:
                 a=0
             else: 
                 a=1 
                 currentValue=alist[j+1]
                 k=j+1
                 
             j=j+1     
         if(a==0):
             #print("here")
             alist[k],alist[s-1]=alist[s-1],alist[k]
         s=s-1       
     
      
def ssort2(alist):
     print("unsorted list is",alist)
     for i in range(0,len(alist)-1):
         min=alist[i+1]
         minIndex=i+1
         for j in range(i+1,len(alist)):
             if alist[j]<min:
                 min=alist[j]
                 minIndex=j
         if min < alist[i]:
            alist[minIndex],alist[i]=alist[i],alist[minIndex]
         print("list after" ,i+1 ,"round",alist)
         
         
alist = [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
ssort2(alist)
#print(alist)            
            