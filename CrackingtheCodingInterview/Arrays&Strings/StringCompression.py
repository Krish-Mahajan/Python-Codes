'''
Created on Dec 23, 2015

@author: Krish

Q:Implement a method to perform basic string compression using the counts of repeated characters.For example,the string aabccccaaa
would become a2b1c5a3.if the compressed string would not become smaller than the original string,your method should return the original string.
 
'''

def  compressString(s):
     if (len(s)==0 or s==None):
         print("No String")
         return -1
     i=0
     comp=""
     
     for ch1 in s[i:]:
         if(i<len(s)):
             #print("here2")
             ch1=s[i]
             count=1
             for ch2 in s[i+1:]:
                 if(ch2==ch1):
                     #print("ch1,ch2",ch1,ch2)
                     count=count+1 
                     i=i+1
                 else:
                     break
                 #print("here")
             comp=comp+ch1+str(count)
             print(comp)
             i=i+1
     if(len(comp)>len(s)):
         return s
     else:
         return comp
         
                                        
     
      
x=compressString("aabcddddd")
print(x)