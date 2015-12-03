'''
Created on Dec 1, 2015

@author: Krish
'''
from collections import defaultdict

def hIndex(citations):
         """
         :type citations: List[int]
         :rtype: int
         """
         if len(citations)<=0:return 0
       
         sort_c = sorted(citations,reverse=True)
         print(sort_c)
         print(citations)
         for i in range(len(sort_c)):
            if i>=sort_c[i]:
                return i
    
         return len(citations) 
     
#h1=hIndex([11,15])
#print (h1) 
h2=hIndex([3,0,6,4,5])
print(h2)