'''
Created on Oct 11, 2015

@author: Krish
'''
def knapsack(W,I):
     l=[0]*(W+1)
     lastItem=[0]*(W+1) 
     print(l)   
     for i in range(1,W+1):
         print("Current KnapSsack Weight is ",i)
         print("Possible Iw's that can be dropped in this Knapsacks is,")
         for iW in [key for key in I if key<=i]:
                 print(iW) 
                 if  I[iW]+ l[i-iW] > l[i]:
                     l[i]=I[iW]+ l[i-iW] 
                     lastItem[i]=iW
                     
                 print(l)
         print("current value list till now is",l)
     print("items used for maximizing",W,"are:")
     printItems(W,lastItem) 

def printItems(W,lastItem):
     #coin = change
     while W > 0:
         thisItem = lastItem[W]
         print(thisItem)
         W = W - thisItem

I={2:3,3:4,4:8,5:8,6:10}
knapsack(15, I)