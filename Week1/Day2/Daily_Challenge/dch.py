# Challange 1
# Ask the user for a number and a length
number = int(input('Type a number'))
length = int(input('Type a length'))
list_length = []

# Create a program that prints a list of multiples of the number until the list length reaches length
for i in range(length):
    new_number = number * (i+1)
    list_length.append(new_number)
print(list_length)

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed
user_word = input('Type your world: ')
new_word = ''
previous_char = ''
for char in user_word:
    if char != previous_char:
        new_word += char
        previous_char = char
print("New word:", new_word)