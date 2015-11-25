'''
Created on Aug 29, 2015

@author: Krish
'''
def msort(alist):
     print("splitting",alist)
     if len(alist)<=1:
         print("heeee")
         return alist
     else:
         mid = len(alist)//2
         print("mid is",mid)
         #lefthalf=alist[:mid]
         #righthalf=alist[mid:]
         lefthalf= msort(alist[:mid])
         righthalf= msort(alist[mid:])
         return merge(lefthalf,righthalf)
         #print("sorted list is",list)

def  merge(lefthalf,righthalf):  
         lhalf=lefthalf
         rhalf=righthalf
         print("In Merge") 
         i=0
         j=0
         k=0
         #print(lhalf[i])
         alistnew =list()
         print("lefthalf is",lhalf,",len lefthalf is",len(lhalf),",righthalf is",rhalf,",len righthalf is",len(rhalf))
         while i<len(lhalf) and j<len(rhalf):
  
             if  lhalf[i] < rhalf[j]:
                 #print("here 1",alistnew[k])
                 alistnew.append(lhalf[i])
                 i=i+1
                 k=k+1
                 print("here 1",alistnew)
                 
                 '''
                  elif lefthalf[i] == righthalf[j]:   
                 alist[k]=lefthalf[i]
                 i=i+1
                 j=j+1
                 k=k+1 
                 print("here 2",alist)
                  '''
                     
             else:
                 alistnew.append(rhalf[j])
                 j=j+1
                 k=k+1
                 print("here 2",alistnew)
     
         while i<len(lhalf):
             alistnew.append(lhalf[i])
             i=i+1
             k=k+1
             print("here 3",alistnew)
         
         while j<len(rhalf):
             alistnew.append(rhalf[j])
             j=j+1
             k=k+1
             print("here 4",alistnew)
         print("Merged ",alistnew)
         return alistnew
alist = [54,26,93,17,77,31,44,55,20]
msort(alist)
#print(alist)
