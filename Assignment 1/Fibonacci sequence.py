number = int(input("Enter your number "))
n1, n2 = 0, 1
count = 0
if number <= 0:
   print("Please enter a positive integer")
   pass
elif number == 1:
   print(n1)
else:
   while count < number:
       print(n1)
       newNum = n1 + n2
       n1 = n2
       n2 = newNum
       count += 1