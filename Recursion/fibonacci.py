'''
Created on Oct 11, 2015

@author: Krish
'''
def recur_fibo(n):
     if n<=1:
         return n
   
     else:
         return (recur_fibo(n-1)+recur_fibo(n-2))
     
     #for i in range(0,n-2):
         #print(i)
         #l[i+2]=l[i]+l[i+1]
     
    
     
# take input from the user
nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))  
         
         
       