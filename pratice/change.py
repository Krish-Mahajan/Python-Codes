'''
Created on Oct 7, 2015

@author: Krish
'''
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
     for cents in range(change+1):
         print("Current change is",cents)   
         coinCount = cents
         newCoin = 1
         x=[]
         for c in coinValueList:
             if c<=cents:
                 x.append(c)
         print("possbile coin value list is",x,"for current change",cents)     
         for j in [c for c in coinValueList if c <= cents]:
             
             print("checking coin value ",j,"for current change",cents)         
             if  minCoins[cents-j] + 1 < coinCount:
                 coinCount = minCoins[cents-j]+1
                 newCoin = j
                 #print("MinCoins for this round is",minCoins)
             minCoins[cents] = coinCount
             coinsUsed[cents] = newCoin
             print("The list of minCoins till now is",minCoins)
             print("coins Used",coinsUsed)
     return minCoins[change]

def printCoins(coinsUsed,change):
     coin = change
     while coin > 0:
         thisCoin = coinsUsed[coin]
         print(thisCoin)
         coin = coin - thisCoin

def main():
     amnt = 21
     clist = [7,3,1]
     coinsUsed = [0]*(amnt+1)
     coinCount = [0]*(amnt+1)
     print("Making change for",amnt,"requires")
     print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
     print("They are:")
     printCoins(coinsUsed,amnt)
     print("The used list is as follows:")
     print(coinsUsed)

main()
