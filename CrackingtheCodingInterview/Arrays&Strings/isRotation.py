'''
Created on Dec 24, 2015

@author: Krish

Q:Assume you have a method isSubstring which checks if one word is a substring of another.Given two string s1 & s2,
write code to check if s2 is a rotation of s1 using only one call to isSubstring(e.g,"Waterbottle" is a rotation of "erbottlewat")
'''

def isRotation(s1,s2):
         if (len(s1)!=len(s2)):
             return False
         else:
             s1s1=s1+s1
             if(s2 in s1s1):
                 return True
             else:
                 return False
             
print(isRotation("Waterbottle","orbetlewatt"))                