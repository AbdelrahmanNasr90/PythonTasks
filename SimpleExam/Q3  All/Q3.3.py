def Fibonacci(n):   
 x, y = 0, 1
 c = 0
 while c < n:
    print(x)
    newNum = x + y 
    x = y
    y = newNum
    c += 1
print("the Fibonacci is ",Fibonacci(10))
