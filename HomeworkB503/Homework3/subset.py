

def makeSum(n,sum,nUsed):
     for no  in n:
         print("no is",no)
         for s in range(1,sum+1):
             
             
             if no==s:
                 nUsed[s]=no 
                 
                                     
            
             elif no<s :
                 if nUsed[s]==0 and s%no!=0:
                     nUsed[s]=nUsed[s-no]+nUsed[no]
                 if nUsed[s]!=s:
                     nUsed[s]=0
         print(nUsed)   
         print("***********************************************")                       
                             
sum=25
n=[8,7,6]
nUsed=[0]*(sum+1)
makeSum(n,sum,nUsed)