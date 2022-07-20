Fizzbuzz = int(input('Enter Your number \n'))
if  Fizzbuzz %3 ==0  and Fizzbuzz %2 ==0:
        print('FizzBuzz')                                        
elif Fizzbuzz %2 == 0:
    print('buzz')
elif Fizzbuzz % 3 == 0 :
    print('Fizz')
else:
 print('Try Again')
