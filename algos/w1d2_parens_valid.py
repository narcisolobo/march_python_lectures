# Parens Valid
# Create a function that, given an input string, returns a boolean whether parentheses in that string are valid. Given input "y(3(p)p(3)r)s", return true. Given "n(0(p)3", return false. Given "n)0(t(0)k", return false.

def parens_valid(input_str):
    parens_stack = []
    for char in input_str:
        if char == '(':
            parens_stack.append(char)
        elif char == ')':
            if len(parens_stack) == 0:
                return False
            else:
                parens_stack.pop()
    return len(parens_stack) == 0

print(parens_valid("y(3(p)p(3)r)s"))
print(parens_valid("n(0(p)3"))
print(parens_valid("n)0(t(0)k"))