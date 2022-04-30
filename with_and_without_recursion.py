#Factorial of a number

#Without recursion:
def fact(number):
  a = 1
  if number ==0 or number ==1:
    return 1
  else:
    for i in range(number):
      a *=i
     return a

number = 5
print(fact(number))


#with recursion:

def fact(number):
  if number ==0 or number ==1: # base case
    return 1
  else:
    a = fact(number - 1) # assumption
     return number * a #proof

number = 5
print(fact(number))
  
# base + assumption + proof

