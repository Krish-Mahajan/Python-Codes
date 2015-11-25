'''
Created on Oct 10, 2015

@author: Krish
'''
def rString(s):
    a=s
    print("a is",a)
    
    if len(s)==1:
         return s
     
    else:
          return s[len(s)-1]+rString(s[:len(s)-1])  
         
     
s=rString("Siri")
print(s)

