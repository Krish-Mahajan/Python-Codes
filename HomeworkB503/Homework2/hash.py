
def hash(alist):
     slots=[[] for i in range(0,9)]
     for i in alist:
         slots[i%9].append(i)    
         print(slots)

alist=[5,28,19,15,20,33,12,17,10]
hash(alist)             