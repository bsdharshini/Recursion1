#9)Find_sum_of_n_natural_number_without_formula.py
""" Formula n(n+1)/2"""

def sum_n(n):
  if n == 0: 
    return 0
  return n + sum_n(n-1)
print(sum_n(5))
