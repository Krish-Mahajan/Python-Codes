'''
Created on Dec 4, 2015

@author: Krish
'''
def maxSubArray(nums):
         """
         :type nums: List[int]
         :rtype: int
         
         """
         '''
         m=nums[0]
         
         for i in range(len(nums)):
             x1=sum(nums[:i])
             x2=sum(nums[i:])
             if(max(x1,x2)>m):
                     m=max(x1,x2) 
                    
             j=len(nums)-1
             while j!=i:
                 x1=sum(nums[i:j])
                 x2=sum(nums[j:])
                 if(max(x1,x2)>m):
                     m=max(x1,x2)
                     
                 j=j-1
                
         return m
         '''
         
         max_ending_here = max_so_far = nums[0]
         for x in nums[1:]:
             max_ending_here = max(x, max_ending_here + x)
             max_so_far = max(max_so_far, max_ending_here)
         return max_so_far
         

s=maxSubArray([-1,-2,-3])
print(s)          