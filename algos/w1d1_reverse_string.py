# snake case
def reverse_string(str):
    reversed = ''
    for i in range(len(str)-1, -1, -1):
        reversed += str[i]
    return reversed

# In Python there are three different types of numbers:
# Integers, Floats, Complex