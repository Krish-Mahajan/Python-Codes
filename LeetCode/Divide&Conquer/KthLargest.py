'''
Created on Dec 4, 2015

@author: Krish
'''
def findKthLargest(nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: int
         """
         
         if len(nums)<=1:
            return nums[0]
         else:
            nums.sort(reverse=True)
            return nums[k-1]
        
nums=[2,1]
k=1
x=findKthLargest(nums, k)
print(x)