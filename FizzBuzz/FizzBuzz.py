numbers = range(1,100)
for num in numbers:
    if num%3 == 0 and num%5 != 0:
        print('Fizz')
    elif num%3 != 0 and num%5 == 0:
        print('Buzz')
    elif num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    else:
        print(num)
