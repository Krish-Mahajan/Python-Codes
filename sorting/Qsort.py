'''
Created on Sep 17, 2015

@author: Krish
'''
def quicksort(myList, start, end):
     #print("the unsorted list is",myList)
     if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
     return myList

def partition(myList, start, end):
     pivot = myList[start]
     left = start+1
     right = end
     done = False
     while not done:
         #print("LeftIndex Before  was",left,"rightIndex before was ",right)
         while left <= right and myList[left] <= pivot:
             left = left + 1
         while myList[right] >= pivot and right >=left:
             right = right -1
         #print("LeftIndex  is",left,"rightIndex is ",right) 
         if  right < left:
             done= True
         else:
            # swap places
             
             myList[left],myList[right]=myList[right],myList[left]
     #print("Left is",myList[left],"right is ",myList[right])        
    # swapp start with myList[right]
     
     myList[start],myList[right]=myList[right],myList[start]  
     print(myList)     
     return right

alist = [5,9,8,10,6,5,11,3,2,1]
list=quicksort(alist, 0, len(alist)-1)
print("the sorted list is",list)
