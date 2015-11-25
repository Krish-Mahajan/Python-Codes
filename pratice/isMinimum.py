
import time
from random import randrange


def findMin(alist):
     min=alist[0]
     for i in alist:
       if i<min:
        min =i      
     return min
'''
def findMin(alist):
   
   for i in alist:
       for  j in alist:
         if i<j:
           overAllMin=i
         else:
           overAllMin=j
           continue
         
   return overAllMin
'''   
            

print(findMin([5,-99,-110,0]))

'''
def findMin(alist):
   overAllMin=alist[0]
   for i in alist:
     isSmallest = True
     for  j in alist:
       if i>j:
        isSmallest=False
        continue
     if isSmallest:
        OverAllmin = i
        
   return OverAllmin
'''

'''
string_input = input("Enter the list of numbers separated by comma : ")
print(string_input)
#string_input = string_input.strip('\t\n\r')
#print(string_input)

#print(type(string_input))
alist = string_input.split(",")
print(type(alist))
print(alist)
print(findMin(alist))
alist = [x.strip(' ') for x in alist]
print(alist)
print(findMin(alist))
'''

'''
for listSize in range(1000,10001,1000):
    alist=[randrange(100000) for x in range(listSize)]
    start=time.time()
    print(alist)
    print(findMin(alist))
    end=time.time()
    print("size: %d time :%f" %(listSize,end-start))
'''    