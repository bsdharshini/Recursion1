#q_Check_number_in_array.py
#without array copying
def check_n(arr,n,s):
    l =len(arr)
    if s == l or l==0:
        return -1
    if a[s] == n:
        return s
    else:
        return check_n(arr,n,s+1)
a = [1,2,3,4]
print(check_n(a,7,0))

#with array copying

def check_n_arr(a,n):
    l = len(a)
    if l ==0:
        return -1
    if a[0]==n:
        return 0
    smallList = check_n_arr(a[1:],n)
    if smallList==-1:
        return -1
    else:
        return smallList+1 # including first element

print(check_n_arr([1,2,3,4],7))