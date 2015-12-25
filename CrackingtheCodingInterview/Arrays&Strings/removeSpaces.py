'''
Created on Dec 24, 2015

@author: Krish

Q4:Write a method to replace all spaces in a string with "%20.You may assume that the string has sufficient space at the end of the
string to hold the additional characters,and that you are given the "true" lenght of the string.
Example
Input: "Mr John Smith  "
Output:"Mr%20John%20Smith"
'''

def removeSpaces(s):
    
     l=[]
     ns=""
     for ch in s:
         if(ch!=" "):
             ns=ns+ch
         else:
             if(ns!=""):
                 l.append(ns)
             ns=""  
         
     if(ns!=""):    
         l.append(ns)   
     #print(l)  
     
     ns=""  
     
     for item in l:
         if(item!=l[-1]):
             ns=ns + item +"%20"
         else:
             ns=ns + item
     print(ns)

removeSpaces("Mr    JohnSmith")             