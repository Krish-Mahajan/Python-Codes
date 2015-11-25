'''
Created on Oct 29, 2015

@author: Krish
'''
'''
Created on Oct 29, 2015

@author: Krish
'''
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