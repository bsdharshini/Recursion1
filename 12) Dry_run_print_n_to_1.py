#12) print_n_to_1.py
# print(n) first then do recursion
def print_1_n(n):
  if n == 0:
    return
  print(n) # first print n then go to recursion
  print_1_n(n-1))
 print_1_n(5)


"""Dry run: 
i) n = 5 
ii) n != 0
iii) print 5
iv) recursion: n = 5-1, go to line 1
v) n =4
vi) n !=0
vii) print 4
viii) recursion: n= 4-1, go to line 1
ix) n = 3
x) n!=0
xi) print 3
xii) recursion: n= 3-1, go to line 1
xiii) n = 2
xiv) n!=0
xv) print 2
xvi) recursion: n= 2-1, go to line 1
xvii) n =1
xviii) n!=0
xix) print 1
xx) recursion: n= 1-1, go to line 1
xxi) n = 0
xxii) n == 0
xxiii) return nothing"""

