
def binarySearch(alist, index):
        first = 0
        last = len(alist)-1
        found = False
   
        while first<=last and not found:
           
           Imidpoint = (first + last)//2
           print(" The list is: ",alist[first:last+1] ," & the index is: ",index,",the value of index is :" ,alist[index],"The Imidpoint is:",Imidpoint)
           if (Imidpoint==index and alist[Imidpoint] == index):
               found = True
               
           else:
                if Imidpoint < index:
                   first = Imidpoint+1
                else:
                   last = Imidpoint-1
   
        return found

testlist = [0,1,2,3,4,5,6,7,8,9]

print(binarySearch(testlist, 9))
