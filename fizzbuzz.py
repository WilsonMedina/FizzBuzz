# Start with some pseudo-code!
#Game Fizz Buzz of 1 to the 100
#always multiplos of 3 write Fizz and for 5 write Buzz
#Always multiplos of 3 and 5 write FizzBuzz


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)