
def getmax(random_list):
     max=random_list[0]
     for i in range(1,len(random_list)):
         if len(max)<len(random_list[i]):        
             max=random_list[i]   
     return max

def  maxd(max): 
     
     count=len(max)
     '''
     while max!=0:
         max=max//10
         count=count+1
     '''    
     return count
     
def radix_sort(random_list):
     max=getmax(random_list)
     maxLen=maxd(max)
     print("max element is",max," and len of max element is",maxLen)
     len_random_list = len(random_list)
     for position in reversed(range(0,maxLen)):
         #print("postion is",position)
         oa = ord('a'); # First character code
         oz = ord('z'); # Last character code
         n = oz - oa + 1; # Number of buckets
         buckets = [[] for i in range(0, n)] # The buckets
         for string in random_list:
             #print("value is", string)
             index=0
             if  position <len(string):
                 index=ord(string[position])-oa
             buckets[index].append(string)
         #print("bucket is",buckets)
         random_list = []
         for x in buckets:
             for y in x:
                 random_list.append(y)
         print(random_list)
         
         
     return random_list    
random_data = ["cow", "dog", "seq", "rug", "row", "mob", "box", "tab", "bar","ear", "tar", "dig", "big", "tea", "now", "fox"]
r=radix_sort(random_data)
print("The sorted list is",r)

