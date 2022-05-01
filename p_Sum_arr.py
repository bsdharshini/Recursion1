#p_sum_of_arr.py
#with arr copying
def sum_arr(a):
  l= len(a)
  if l ==0:
    return 0
  if l == 1:
    return a[0]
  return a[0]+sum_arr(a[1:])

print(sum_arr([2,4,6,1]))
  