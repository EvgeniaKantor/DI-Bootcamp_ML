# user_name = input('What is your name?')
# if user_name == 'Evgenia':
#     print("We have the same name!")
# else:
#     print('We have different names!')

user_number = int(input('Print a number between 1 and 100:'))
if user_number % 3 == 0 and user_number % 5 == 0:
    print('FizzBizz')  # First check for multiples of both 3 and 5
elif user_number % 3 == 0:
    print('Fizz')
elif user_number % 5 == 0:
    print('Bizz')
else:
    print('Try again!')