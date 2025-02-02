# Exercise 1
# Print 'Hello word' * 4 in one line of code
print('Hello word \n' * 4)

# Exercise 2
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8)
print((99**3)*8)

# Exercise 3
# Predict the output of the following code snippets
print(5 < 3) #False
print(3 == 3) #True
# print(3 == "3") #Error
# print("3" > 3) #Error
print("Hello" == "hello") #False

# Exercise 4
# Create a variable called computer_brand which value is the brand name of your computer
computer_brand = 'ASUS'

# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer"
print(f'I have a {computer_brand} computer')

# Exercise 5
# Create a variable called name, and set it’s value to your name
name = 'Evgenia'

# Create a variable called age, and set it’s value to your age
age = 40

# Create a variable called shoe_size, and set it’s value to your shoe size
shoe_size = 39

# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3
info = f"My name is {name}, I'm {age} years old, my shoe size is {shoe_size}"

# Have your code print the info message
print(info)

# Exercise 6
# Create two variables, a and b. Each variable value should be a number
a = 5
b = 3
# If a is bigger then b, have your code print Hello World.
if a > b:
    print('Hello world!')
else:
    print('Oh no!')

# Exercise 7
# Write code that asks the user for a number and determines whether this number is odd or even
new_number = int(input('What is your number?'))
if new_number == 0:
    print('This number is neither even nor odd')
elif new_number % 2 == 0:
    print('This number is odd number')
else:
    print('This number is even number')

# Exercise 8
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome

your_name = input('What is your name?')
if your_name.lower() == name.lower():
    print('Great! We have the same name!')
else:
    print('Nice to meet you!')

# Exercise 9
# Write code that will ask the user for their height in centimeters
your_height = int(input('What is your height in cm? Please print only the number'))
# If they are over 145cm print a message that states they are tall enough to ride. If they are not tall enough print a message that says they need to grow some more to ride.

if your_height > 145:
    print('You are tall enough to ride')
else:
    print('You need to grow some more to ride')