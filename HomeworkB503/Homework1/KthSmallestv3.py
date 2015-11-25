'''
Created on Sep 10, 2015

@author: Krish
'''
def kthlargest(arr1, arr2, k):
     if len(arr1) == 0:
        return arr2[k]
     elif len(arr2) == 0:
        return arr1[k]

     mida1 = len(arr1)//2
     mida2 = len(arr2)//2
     print("arr1 is",arr1,",mid index arr1 is",mida1,",middle element is",arr1[mida1])
     print("arr2 is",arr2,"mid index arr2 is",mida2,",middle element is",arr2[mida2])
     print("k is",k)
     
     if mida1+mida2<k:
        if arr1[mida1]>arr2[mida2]:
            return kthlargest(arr1, arr2[mida2+1:], k-mida2-1)
        else:
            return kthlargest(arr1[mida1+1:], arr2, k-mida1-1)
     else:
        if arr1[mida1]>arr2[mida2]:
            return kthlargest(arr1[:mida1], arr2, k)
        else:
            return kthlargest(arr1, arr2[:mida2], k)
        
alist1=[9,18,20,21,25,30,31,34]
alist2=[1,2,13,14,16,19,20]
k=2
x=kthlargest(alist1, alist2, k)
print(k," largest no is",x)
