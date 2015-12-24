'''
Created on Dec 23, 2015

@author: Krish
'''
'''
Q:Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
-should ask interviewer if its ASCII string or Unicode string
-ASCII defines 0-255 characters,unicode defines 0-2^21.ASCII is subset of unicode.
- if len(s)>256 return False
'''

## Using a Data structure O(n)
def uniqueData(s):
     if(len(s)==0 or s==None):
         print("NO String")
         return -1
     if(len(s)==1):
        return True
    
     d={}
     for ch in s:
         if ch in d:
             d[ch]=d[ch]+1
         else:
             d[ch]=1    
             
     for key in d:
         if(d[key]>1):
             return False
         
     return True

x=uniqueData("abcdefgh")
print(x) 

###without a data Structure  O(n^2)
def  unique(s):
     if(len(s)==0 or s==None):
         print("NO String")
         return -1
     if(len(s)==1):
        return True
     i=0    
     for ch1 in s:
         for ch2 in s[i+1:]:
             if  ch1==ch2:
                 print(ch1)
                 return False     
         i=i+1
     return True
   
x=unique("abcdefgh")  
print(x)        