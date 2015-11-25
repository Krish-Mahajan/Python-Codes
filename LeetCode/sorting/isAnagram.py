'''
Created on Nov 24, 2015

@author: Krish
'''

def isAnagram(s,t):
     listsc=dict.fromkeys(list(s))
     listtc=dict.fromkeys(list(t))
     
     for key in listsc.keys():
         listsc[key]=0
         
     for key in listtc.keys():
         listtc[key]=0   
     
     #print(listsc)
     #print(listtc)
     result=True
     if(len(s)!=len(t)):
         return False
     
     for item in list(t):
         listtc[item] +=1
         
         
     for item in list(s):
         listsc[item] +=1
         
     #print(listtc)     
     #print(listsc) 
     
     for key in listtc.keys():
              if(not(key in listsc.keys() and listsc[key]==listtc[key])):
                result=False  
                
     return result
 
 
print(isAnagram("aacc","ccac"))