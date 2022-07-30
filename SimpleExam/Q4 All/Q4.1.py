import numbers
import string 
import random

digit = list(string.digits)
uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
def generatePassword():
    passwordLength = input("Enter password length =  ")
    while True:
        try:
            passwordLength = int(passwordLength)
            if passwordLength < 10 :
                print("must 10 char")
                passwordLength = int(input("Enter password length : "))
            break
        except:
            print(" enter numbers only ")
            passwordLength = int(input('Enter password length: '))
            
    password = []
    random.shuffle(uppercase)  
    random.shuffle(lowercase)  
    random.shuffle(digit)   



    for i in range(round(passwordLength * .4)):
        password.append(uppercase[i])


    for i in range(round(passwordLength * .3)):
        password.append(lowercase[i])


    for i in range(round(passwordLength * .3)):
        password.append(digit[i])


    password = "".join(password[0:])


    print("Your password is = ", password)

generatePassword()