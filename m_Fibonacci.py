# Fibonacci of 7 -> 1, 1, 2, 3, 5, 8, ,13 -> n1+n2 = n3
def fib(n):
  if n==0:
    return 0
  if n == 1:
    return 1
  return fib(n-1)+fib(n-2)
