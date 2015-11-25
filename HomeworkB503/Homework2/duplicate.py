'''
Created on Aug 29, 2015

@author: Krish
'''
def msort(alist):
     
     if len(alist)<=1:
         return alist
     else:
         mid = len(alist)//2
         lefthalf= msort(alist[:mid])
         righthalf= msort(alist[mid:])
         return merge(lefthalf,righthalf)

def  merge(lefthalf,righthalf):  
         lhalf=lefthalf
         rhalf=righthalf
         i=0
         j=0
         alistnew =list()
         while i<len(lhalf) and j<len(rhalf):
  
             if  lhalf[i] < rhalf[j]:
                 alistnew.append(lhalf[i])
                 i=i+1
             elif lefthalf[i] == righthalf[j]:   
                 alistnew.append(lefthalf[i])
                 i=i+1
                 j=j+1
                   
             else:
                 alistnew.append(rhalf[j])
                 j=j+1
                 
         while i<len(lhalf):
             alistnew.append(lhalf[i])
             i=i+1        
         while j<len(rhalf):
             
             alistnew.append(rhalf[j])
             j=j+1        
         return alistnew
alist = [54,26,26,77,0,9,9,9,93,17,77,77,31,31]
print("Unsorted duplicate list:")
print(alist)
l=msort(alist)  
print("sorted non duplicate list:")
print(l)      
             
             
         
         
             
             
             
                 
                 
                 
             
                
                     
             
     

#print(alist)
