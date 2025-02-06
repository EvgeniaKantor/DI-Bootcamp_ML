matrix_string = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
"""
print(matrix_string)

# Creat a 2D list
matrix = []

lines = matrix_string.strip().split("\n")
print(lines)

for line in lines:
    matrix.append(list(line))
print(matrix)

num_cols = len(matrix[0])
print(num_cols)

# Decrypt the matrix: for loop for checking characters
# Replace every group of symbols between two alpha characters
decoded_message = ""
for col in range(num_cols):
    for row in range(len(matrix)):  
        char = matrix[row][col]
        if char.isalpha():
            decoded_message += char
        else:
            if len(decoded_message) != 0 and decoded_message[-1] != ' ':
                decoded_message += " "

print("Decoded Message: ", decoded_message)

cleaned_message = " ".join(decoded_message.split())
# cleaned_message = decoded_message.strip()
print("Decoded Message:", cleaned_message)