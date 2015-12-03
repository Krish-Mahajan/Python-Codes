'''
Created on Dec 2, 2015

@author: Krish
'''
def largestNumber(nums):
         """
         :type nums: List[int]
         :rtype: str
        """
         if(len(nums)==0):
             return nums
         
         
         ml=[] #list of list
         for i in nums: 
             l=[] #list to hold individual digits of no
             for ch in str(i):
                 l.append(ch)
             ml.append(l)  
         #del l[:]
         ln="" #Largest Number
        
         
         ml.sort(reverse=True)
         print(ml)
         
             
         def my_cmp(l1,l2):     
             l1=''.join(str(n) for n in ml[0]) 
             l2=''.join(str(n) for n in ml[1])
             if(int(l1+l2)>int(l2+l1)):
                 return l1+l2
             return l2+l1
                 
         while (len(ml)!=0):
             if(len(ml)>1):
                 x1=ml[0][0][0]
                 x2=ml[1][0][0]
                 if(x1==x2):
                    x =my_cmp(ml[0],ml[1])
                    ln=ln+str(x)
                    print(ln)
                    del ml[:2]
                 else:   
                     if(len(ml)>0):
                         x=int(''.join(map(str,ml[0])))
                         ln=ln+str(x)
                         print(ln)
                         ml.remove(ml[0])
             if(len(ml)==1):
                 x=int(''.join(map(str,ml[0])))
                 ln=ln+str(x)
                 print(ln)
                 ml.remove(ml[0])
                 
              
         if(int(ln)==0):
            return str(0)        
         return ln     
         
nums1=[824,938,1399,5607,6973,5703,9609,4398,8247]
ln=largestNumber(nums1) 
print(ln)
'''
nums=[10,2]
ln=largestNumber(nums) 
print(ln)
'''
