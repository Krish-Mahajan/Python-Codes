'''
Created on Nov 29, 2015

@author: Krish
'''
import random
def sortColors(nums):
         """
         :type nums: List[int]
         :rtype: void Do not return anything, modify nums in-place instead.
         """
         """
         We can do this problem by counting sort too
         """
         """
         red, white, blue = 0, 0, 0
         for i in range(len(nums)):
             if nums[i] == 0:
                 red += 1 
             elif nums[i] == 1:
                 white += 1
             elif nums[i] == 2:
                  blue += 1
         for h in range(red):
             nums[h] = 0
         for j in range(red, red + white):
             nums[j] = 1
         for k in range(red + white, red + white + blue):
             nums[k] = 2
         """
         max=nums[0]
         for i in range(0,len(nums)):
             if  nums[i]>max:
                 max=nums[i]
         print("max element is",max)        
         
         c=[0]*(max+1)
         print(c)
         for value in nums:
             c[value]=c[value]+1
         print("c initially is",c) 
       
         for i in range(1,len(c)):
             c[i]=c[i-1]+c[i]
         print("c now is",c)    
         
         sorted_nums=[0]*len(nums)
         for i in reversed(range(0,len(nums))):
             sorted_nums[c[nums[i]]-1]=nums[i] 
             c[nums[i]]=c[nums[i]]-1
             print("sorted list is ",sorted_nums)    
         nums=sorted_nums                                  

nums1=[0,1,]  
 
sortColors(nums1)

     
             