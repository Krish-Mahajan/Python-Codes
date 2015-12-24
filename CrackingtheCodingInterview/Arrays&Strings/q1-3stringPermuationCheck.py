'''
Created on Dec 23, 2015

@author: Krish

Q:Given two strings,write a method to decide if one is a permutation of other
-Assuming case sensitive
-Assuming whitespaces as part of string
'''
def permuationCheck(s1,s2):
         if (len(s1)!=len(s2)):
             return False;
         d1=countEachCh(s1)
         d2=countEachCh(s2)
         return(d1==d2)
         
def countEachCh(s):
     d={}
     for ch in  s:
         if ch in d:
             d[ch]=d[ch]+1         
         else:
             d[ch]=1
     return d     
 
s1="abbada"       
s2="aaabcdee"
ans=permuationCheck(s1, s2)
print(ans)