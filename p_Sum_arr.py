#p_sum_of_arr.py
#with arr copying
def sum_arr1(a):
  l= len(a)
  if l ==0:
    return 0
  if l == 1:
    return a[0]
  return a[0]+sum_arr1(a[1:])

print(sum_arr1([2,4,6,1]))

#without arr copying

def sum_arr(a,s):
  l= len(a)
  if s == l:
    return 0
  return a[s]+sum_arr(a,s+1)
a = [2,4,6,1,5]
print(sum_arr(a,0))
  