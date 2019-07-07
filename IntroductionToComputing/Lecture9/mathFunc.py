from _ast import Num

def summation(numbers):
    total = 0
    for num in numbers :
        total += num 
    return total 


def mean(numbers): 
    total = 0.0 
    for num in numbers:
        total +=num 
    return total/len(numbers)


#test code

if __name__ == "__main__" :
    nums=[1,2,3,4]
    print(summation(nums) == 10)
    print(mean(nums) == 2.5)