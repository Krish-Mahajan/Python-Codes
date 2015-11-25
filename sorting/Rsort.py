
def getmax(random_list):
     max=random_list[0]
     for i in range(1,len(random_list)):
         if max<random_list[i]:        
             max=random_list[i]   
     return max

def  maxd(max): 
     count=0
     while max!=0:
         max=max//10
         count=count+1
     return count
     
def radix_sort(random_list):
     max=getmax(random_list)
     count=maxd(max)
     len_random_list = len(random_list)
     modulus = 10
     div = 1
    
     while count!=0:
        # empty array, [[] for i in range(10)]
         print("count is",count)
         new_list = [[], [], [], [], [], [], [], [], [], []]
         for value in random_list:
             #print("value is", value)
             least_digit = value % modulus
             least_digit= least_digit//div
             new_list[least_digit].append(value)
             #print("New list is",new_list)
         modulus = modulus * 10
         div = div * 10
         print(new_list)
         #break
     
         #if len(new_list[0]) == len_random_list: ## Array got sorted
         #return new_list[0]

         random_list = []
         #rd_list_append = random_list.append
         #print("rd_list_append is",rd_list_append)
         for x in new_list:
             #print("x is ",x)
             for y in x:
                #print("y is",y)
                random_list.append(y)
                #print("random list is ",random_list)
         print("random list is ",random_list)
         count=count-1
     return random_list  
 
import random
random_data= random.sample(range(100), 10)
#[3, 1, 21, 19]   
#random_data = [100000,9000,600,450,30,1,0]
print("Random_data is",random_data)
radix_sort(random_data)
#print(r)

#radix_sort([10000, 1000, 100, 10, 0])