# Python Interpreter
# To enter the Python interpreter, or shell, simply type python in your terminal or command prompt.
# Your prompt should turn into three greater than symbols. You are now in the Python shell and can enter and execute Python code.

# Some differences between JavaScript and Python numbers:
# JavaScript treats integers and floats as the same datatype - numbers.
# Python treats them as separate datatypes.

ounces_in_a_cup = 8
type(ounces_in_a_cup) # output - integer
pi = 3.14
type(pi) # output - float

# Python does not have the ++ or -- operator.
num = 1
num += 1 # increment by one in Python
num -= 1 # decrement by one in Python 

# Every time you divide two numbers in Python, the result is a float.

result = 4 / 2
print(result) # output - 2.0
print(type(result)) # output - <class 'float'>

# Python has the floor division operator //, which chops off everything after the decimal point.

result = 4 // 2
print(result) # output - 2
type(result) # output - <class 'int'>

# Strings
# Strings behave just like they do in JavaScript.

# They are also immutable.
my_name = 'Narciso'
my_name[0] = 'Z' # TypeError: 'str' object does not support item assignment

# Each character in a string can be referenced by its index.
word = 'Python is an interpreted language'
word[0] # output - 'P'

# You can even go backwards by using negative index numbers.
word[-1] # last character in string - output -> 'e'
word[-2] # second to last character in string - output -> 'g'

# Strings can be sliced.
word[1:6] # will output the characters from index 1 to 5 (the ending number is exclusive). Output - 'ython'

# To force certain character to behave as strings and not code, you can use the escape character - \

word_with_escape = 'I won\'t tell'

# You can put line breaks by using \n
print('first line\nsecond line')

# When needed, you can preface the first quotation mark with an r to make a 'raw string'
path = print('C:\some\name') # SyntaxError: invalid syntax
path = print(r'C:\some\name') # Use r to make it raw

# You can concatenate strings
word = 'Python '
another_word = 'is cool!'

print(word + another_word) # output - Python is cool!

# You can multiply string by a number
print('*'*100)
# output - ****************************************************************************************************

# Compound datatypes
# Lists, Dictionaries, Tuples, Sets

Lists are bookended by square brackets []
Dictionaries are bookended by {} AND they have key-value pairs.
Tuples are bookended by parentheses () and they are immutable.
Sets are bookended by curly braces {} and they are immutable and disallow duplication of values.

# Concatenate lists

# my_list = [1, 2, 3, 4]

# print(my_list + [5, 6, 7])

# students = [
#     {
#         'name': 'Jagdeep Singh',
#         'class': 'Python Stack'
#     },
#     {
#         'name': 'Nathan Bludworth',
#         'class': 'MERN Stack'
#     }
# ] 

for student in students:
    print(student['name'])

for i in range (len(students)):
    print(students[i]['name'])

# my_tuple = (1, 2, 3, 4, 7)
# print(my_tuple)

# my_list_of_nums = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7]
# my_list_of_nums = set(my_list_of_nums)
# print(my_list_of_nums)
# my_list_of_nums = list(my_list_of_nums)
# print(my_list_of_nums)

# my_list_of_nums = tuple(my_list_of_nums)
# print(my_list_of_nums)

# my_set = {3, 6, 1, 8, 9}

# If Statements
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for statements