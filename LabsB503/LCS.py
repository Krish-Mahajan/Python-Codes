'''
Created on Nov 12, 2015

@author: Krish
'''
'''
Created on Oct 29, 2015

@author: Krish
'''
def lcs(S,T):  # LCS using dynamic Programming
     m = len(S)
     n = len(T)
     counter = [[0]*(n+1) for x in range(m+1)]
     longest = 0
     lcs_set = set()
     for i in range(m):
         for j in range(n):
             if S[i] == T[j]:
                 c = counter[i][j] + 1
                 counter[i+1][j+1] = c
                 if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                 elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])
     return lcs_set               
# test 1
ret = lcs('academy', 'abracadabra')
for s in ret:
    print(s)

# test 2
#ret = lcs('ababc', 'abcdaba')
#for s in ret:
   # print(s)                    
   
################################################################################################################   
def lcs_r(str1, str2): #LCS using recurrence
  # If either string is empty, stop
  if len(str1) == 0 or len(str2) == 0:
    return ""
  
  # First property
  if str1[-1] == str2[-1]:
    return lcs_r(str1[:-1], str2[:-1]) + str1[-1]
    
  # Second proprerty
  # Last of str1 not needed:
  t1 = lcs_r(str1[:-1], str2)
  # Last of str2 is not needed
  t2 = lcs_r(str1, str2[:-1])
  if len(t1) > len(t2):
    return t1
  else:
    return t2
    
if __name__ == "__main__":
  print(lcs_r('academya','abracadabra'))        