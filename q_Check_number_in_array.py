#q_Check_number_in_array.py

def check_n(arr,n,s):
    l =len(arr)
    if s == l:
        return False
    if a[s] == n:
        return s
    else:
        return check_n(arr,n,s+1)
a = [1,2,3,4]
print(check_n(a,7,0))