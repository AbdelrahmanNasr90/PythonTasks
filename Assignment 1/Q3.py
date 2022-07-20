# 1)
from ast import Pass
from unittest import result
x = input('Enter your number')
y = ""
for i in x:
    y = i + y

if (x == y):
    print("Yes")
else:
    print("No")

# 2) 
def Rlist(list1,list2):
   resultlist=[]
   list1 = [10, 20, 25, 30, 35] 
   list2 = [40, 45, 60, 75, 90] 

   for i in list1:
      if i%2 != 0 :
         resultlist.append(i)
   for j in list2:
       if j%2==0 :
         resultlist.append(j)  
   return resultlist

# 3)
def exponent(base, exp):
    x = exp
    result = 1
    while x > 0:
        result *= base
        x = x - 1
    print(result)

# 4) 
x = int(input('Enter your number'))
for i in range (1,101):
    print(i * x)

# 5)
list_numbers = []
n = int(input("Enter number of elements : "))  
for i in range(0, n):
    sum = int(input())
    list_numbers.append(sum)
x = len(list_numbers) 
while x >= 0 :
    print(list_numbers[x]) 
    x -= 1

# 6)
x= int(input("Enter your start "))
y= int(input("Enter your END "))
for i in range (x,y+1):
    if i >1:    
     if i%2==0:
         pass
     else:
        print(i)
    else:
        Pass    


# 7)
for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        pass
    elif fizzbuzz % 3 == 0:
        print("fizz")
        pass
    elif fizzbuzz % 5 == 0:
        print("buzz")
        pass
    print(fizzbuzz)

# 8)

x = (True, True, True)
result = all(x)
print(result)

x = (True, True, False)
result = all(x)
print(result)