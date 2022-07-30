def recur(number):
    if number<1:
        print("Enter positive number plz")
    elif number == 1:
        return number
    else:
        return number + recur(number-1)
x=int(input("Enter your number "))   
print(recur(x))

