'''
Created on Sep 10, 2015

@author: Krish
'''
def kthsmallest(m,n,k):
     s1=len(m)  #length list1
     s2=len(n)  #length list2
     
     if(k<s1):
         m=m[:k] #rejecting all list indices greater than K in list2     
     if(k<s2):
         n = n[:k] #rejecting all list indices greater than K in list1
    
     print("m is",m,"middle element of m is",m[(len(m)//2)])
     print("n is",n,"middle element of n is",n[(len(n)//2)])    
     #print(len(alist1)//2)-1 + (len(alist2)//2)-1)
     y=k
     while  (len(m)//2)+ (len(n)//2)>k:
         print("Here1")     
         if m[len(m)//2]> n[len(n)//2]:
             m=m[:(len(m)//2)]
             #print(m)
         else:
             n=n[:(len(n)//2)]
             #print(n)
         
         
     
     print("m is",m,"middle element of m is",m[(len(m)//2)])
     print("n is",n,"middle element of n is",n[(len(n)//2)]) 
     x=k
     while  (len(m)//2)+ (len(n)//2) <= k and x!=0:
          print("Here2")
          print("m is",m,"middle element of m is",m[(len(m)//2)])
          print("n is",n,"middle element of n is",n[(len(n)//2)])
          #print("Middle element of m is",m[len(m)//2-1])
          #print("Middle element of n is",n[len(n)//2-1])
          
          print("x is",x)
          if m[len(m)//2]> n[len(n)//2]:
             if(x==2):
                 print("K smallest element is",n[len(n)//2-1])
                 break
             y= len(n[:len(n)//2])
             n=n[len(n)//2:]
             
          else:
             if(x==2):
                 print("K smallest element is",m[len(m)//2-1])
                 break 
             y= len(m[:len(m)//2])
             m=m[len(m)//2:]
                          
             
          x=x-y
          
    
alist1=[9,18,20,21,25,30,31,34]
alist2=[1,2,13,14,16,19,20]
kthsmallest(alist1, alist2, 14)