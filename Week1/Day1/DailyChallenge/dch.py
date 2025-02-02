import random
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# Then, print the first and last characters of the given text

your_string = input('Please write a string 10 characters long: ')
if len(your_string) > 10:
    print('string too long')
elif len(your_string) < 10:
    print('string not long enough')
else:
    print('perfect string')
    print(your_string[0])
    print(your_string[-1])


# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
constructed_string = ''
for char in your_string:
    constructed_string += char
    print(constructed_string)

# Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
char_list = list(your_string)
random.shuffle(char_list)
new_string = ''.join(char_list)
print(new_string)

