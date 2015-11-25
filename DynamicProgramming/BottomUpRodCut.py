'''
Created on Oct 7, 2015

@author: Krish
''' 


def Revenue(priceList,size,maxRevenue,rodsUsed):
     for rodSize in range(1,size+1):
         print("RodSize is",rodSize,"Revenue as listed for this RodSize is",priceList[rodSize])
         maxRevenue[rodSize]=priceList[rodSize]
         newRodSize=rodSize
         for i in range(1,rodSize+1):
             print("i is",i)
             q=priceList[i]+ maxRevenue[rodSize-i]
             print("q(revenue calculated from subproblem) is",q,"for i",i,"and rodSize",rodSize)
             if q>maxRevenue[rodSize]:
                 maxRevenue[rodSize]=q
                 newRodSize=i
             rodsUsed[rodSize]=newRodSize    
         print("Revenue list till now",maxRevenue)
         print("Last RodSize used ",rodsUsed)
     return maxRevenue[size]

def  printRods(rodsUsed,rodSize):
     while rodSize>0:
         thisRodSize=rodsUsed[rodSize]
         print(thisRodSize)
         rodSize=rodSize-thisRodSize
         
priceList=[0,1,5,8,9,10,17,17,20,24,30]
maxRevenue=[0]*len(priceList)

rodSize=9
rodsUsed=[0]*len(priceList)
#print(rodList)
x=Revenue(priceList, rodSize, maxRevenue,rodsUsed)
print("Max Revenue we can generate by cutting rods of",rodSize," inches is",x)
print("DIfferent rods used")
printRods(rodsUsed, rodSize)