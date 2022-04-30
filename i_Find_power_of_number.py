# 5^4 -> 5 * 5 * 5 * 5 -> 5*fn(5,4-1)
def power_n(n,x):
  if x == 0:
    return 1
  return n * power_n(n,x-1)
print(power_n(5,4))
