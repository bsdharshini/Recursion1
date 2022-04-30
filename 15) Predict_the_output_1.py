def fn(n):
  if n==4:
    return n
  else:
    return 2*fn(n-1)
 print(fn(2))


# o/p 16 

""" Dry run:
i) n =2
ii) n !=4
iii) 2 * fn(2+1)
iv) n =3
v) n !=4
vi) 2*2*fn(3+1)
vii) n =4
viii) n==4
ix) return 4
x) 2 * 2 * 4 -> 16"""
