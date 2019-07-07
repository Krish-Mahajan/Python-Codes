

#Default Arguments, Keyword Arguments , modules , tools.py

import mathFunc

def birthday(name="joe" , age =21):
    print("Happy Birthday", name,"! You're" , age, "!")
    
    
birthday()
birthday("Mary",25)
birthday(22)
birthday(age=22) 
'''
birthday(name = "Mike", 10)
'''

strings = [ 'C' , 'a' , 'B','d','e','F']
copy = strings.copy() 
strings.sort()
copy.sort(key = str.lower , reverse = True)
print("Strings:" , strings);
print("Copy", copy) 

'''
def birthday2(name = "Mike" , age): 
    print("Happy Birthday" , name , "! You're",age,"!")
''' 


print(mathFunc.summation([1,2,3,4]))