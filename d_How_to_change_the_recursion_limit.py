#Default recursion limit is '1000'

#How_to_change_the_recursion_limit

import sys as s
print(s.recursionlimit()) # print the default limit
s.setrecursionlimit(3000)# sets new limit
def limits():
  print('hello')
  limits() # prints least 3000 times
limits()
