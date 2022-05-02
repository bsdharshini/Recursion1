#r_Find_last_index.py

def last_index_copy(a,n):
    l = len(a)
    if l == 0:
        return -1
    smallList = last_index_copy(a[1:],n)
    if smallList == -1:
        if a[0]==n:
            return 0
        else:
            return -1
    else:
        return smallList+1
a = list(int(i) for i in input().strip().split())
n = int(input())
print(last_index_copy(a,n))

"""dry run: a = [1,2,3,4,3,4,8] n =4
i) ([1,2,3,4,3,4,8],4)
ii) ([2,3,4,3,4,8],4)
iii) ([3,4,3,4,8],4)
iv) ([4,3,4,8],4)
v) ([3,4,8],4)
vi) ([4,8],4)
vii) ([8],4)
viii) ([],4) -> l == 0 so returns -1
ix) smallList == -1 so,
x) check a[0] == n
xi) viii) return -1, vii) return -1, vi) return 0
xi) smallList+1 -> v+iv+iii+ii+i = 1+1+1+1+1 = 5
so answer =5
"""

#without copying an array

def last_index(a,n,s):
    l =len(a)
    if s ==l:
        return -1
    smallList = last_index(a,n,s+1)
    if smallList == -1:
        if a[s]==n:
            return s
        else:
            return -1
    else:
        return smallList+1

a = list(int(i) for i in input().strip().split())
n = int(input())
print(last_index(a,n,0))