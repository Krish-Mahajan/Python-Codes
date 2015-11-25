'''
Created on Oct 10, 2015

@author: Krish
'''

def isPalindrome(s):
     if len(s)<2:
         return True
     
     else:
         if s[0]==s[len(s)-1]:
             return isPalindrome(s[1:len(s)-1])       
         else:
             return False
         
         
x=isPalindrome("hannah")
print(x)        