# # user_info = {'name': 'Ron', 
# #              'last_name': 'Weasley',
# #              'age': 17,
# #              'adress': 'Ottery Village - England',
# #              'family': [('Arthur', 'Father', 50), ('Molly', 'Mother', 48)],
# #              'hobbies': {'Quidditch', 'Swimming'}
# #              }
# # print(user_info['name'])
# # print(user_info['family'][0])

# # sample_dict = { 
# #    "class":{ 
# #       "student":{ 
# #          "name":"Mike",
# #          "marks":{ 
# #             "physics":70,
# #             "history":80
# #          }
# #       }
# #    }
# # }

# # print(sample_dict["class"]["student"]["marks"]["history"])

# student_info = {
#     'name': 'John',
#     'age': 25,
#     'hobbies': ['reading', 'gaming', 'cycling'],
#     'city': 'New York'
# }

# # Tasks:
# # 1 - Change the value of 'age' from 25 to 30.
# # 2 - Add a new entry with the key 'occupation' and the value 'Engineer'.
# # 3 - Remove the entry with the key 'city'.
# # 4 - check if the key 'email' is on the dictionary, if not, add it with value 'name@gmail.com'
# # 5 -Loop through the values in the 'hobbies' list and print each hobby on a new line.

# student_info['age'] = 30
# print(student_info)
# student_info['occupation'] = 'Engineer'
# print(student_info)
# del student_info['city']
# print(student_info)
# print('email' in student_info)
# if 'email' not in student_info:
#     student_info['email'] = 'name@gmail.com'
# print(student_info)
# for hobby in student_info['hobbies']:
#     print(hobby)

# student_info['hobbies'].append('soccer')
# print(student_info)

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    if key in sample_dict:
        del sample_dict[key]
    else:
        print('There is not the key in the dict')

print(sample_dict)