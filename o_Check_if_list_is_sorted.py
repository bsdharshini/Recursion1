#o_Check_if_list_is_sorted.py
def isSorted(arr):
  l = len(arr)
  # base case list with len 1 or 0 return true. Because it is already sorted
  if l == 0 or l == 1:
    return True
  # small case or assumption arr[l-1] is true
  smallList = arr[1:]
  
  # condition a[0] < a[1] then call fn from 1 i.e. a[1:]
  if a[0]<a[1]:
    answer = isSorted(smallList)
  else:
    return False
  return answer
a = [2,4,1]
print(isSorter(a))

#o/p False

# This solution is not recommended since it is slicing and creating n number of array

# So with existing array using index call the recursive fn

# Recommened solution

def isSorted(arr,s):
  l = len(arr)
  # base case list with start index is equal to len(arr) return true. Because all the elements are already sorted
  if s == l-1:
    return True
  # condition a[0] < a[1] then increment s by 1 i.e. s+1. Then call the recursive fn
  if a[s]<a[s+1]:
    answer = isSorted(arr,s+1)
  else:
    return False
  return answer
a = [2,4,6]
print(isSorted(a,0)) # default start and end index is 0 and len(a)
  
