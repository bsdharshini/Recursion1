#13) print_odd_num.py
def odd(n):
  if n <= 0:
    return
  if n%2 == 0:
    odd(n-1)
  else:
    odd(n-2)
   print(n)
  
  # if n is odd n-2 eg: if n=5 then next n should be 3 so n-2
  # if n is even n-1 eg: if n=4 then next should be 3 so n-1
  
