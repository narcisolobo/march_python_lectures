# import random

# returns a random floating number between 0.000 and 1.000
# random.random()

# returns a random floating number between 0.000 and 50.000
# random.random() * 50

# returns a random floating number between 10.000 and 35.000
# random.random() * 25 + 10

# returns the rounded integer value of num
# round(num)

# PLAN OUR ATTACK WITH PSEUDOCODE
# Declare a function named rand_int that has a default min value of 0 and a default max value of 100.
# Create a random floating point number between 0 and 1 using random.random and store it in a variable called num.


# def randInt(min=0, max=100):
#     num = round(random.random() * (max - min) + min)
#     return num


# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
# print(randInt(min=100, max=50))


# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# def iterate_list_of_dictionaries(list_of_dictionaries):
#     for dictionary in list_of_dictionaries:
#         output = ''
#         for key, value in dictionary.items():
#             output += f'{key} - {value}, '
#         print(output)

# iterate_list_of_dictionaries(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]


x[1][0] = 15
# print(x)

for i in range(len(students)):
    for trait in students[i]:
        if students[i][trait] == 'Jordan':
            students[i][trait] = 'Bryant'

# print(students)


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
# In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [{'x': 10, 'y': 20}]
# Change the value 20 in z to 30

z[0]['y'] = 30

print(z)