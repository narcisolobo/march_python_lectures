# Recursive Functions
# 1. Base Case
# 2. Forward Progress
# 3. Calling Back Into Itself

# Recursive Sigma
# Write a recursive function that takes in an integer and returns the sum of all previous integers.

# First, a linear solution:
def sigma(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum
print(f'Linear sigma: {sigma(6)}')

# Now, a recursive solution:
def r_sigma(num):
    if (num < 1):
        return 0
    else:
        return num + r_sigma(num - 1)
print(f'Recursive sigma: {r_sigma(6)}')

# Recursive Factorial
# Write a recursive function that takes in an integer and returns the product of all previous integers.

# First, a linear solution:
def facto(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
        print(product)
    return product
print(f'Linear factorial: {facto(6)}')

# Now, a recursive solution:
def r_facto(num):
    if (num == 1):
        return 1
    else:
        return num * r_facto(num - 1)
print(f'Recursive factorial: {r_facto(6)}')

# Recursive Fibonacci
# Write a recursive function that takes in an index and returns the value of a Fibonacci sequence at that index.

# First, a linear solution:
def fib(idx):
    sequence = [0, 1]
    for i in range(2, idx + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[idx]
print(f'Linear Fibonacci: {fib(6)}')

# Now, a recursive solution:
def r_fib(idx):
    if (idx < 2):
        return idx
    else:
        return r_fib(idx - 1) + r_fib(idx - 2)
print(f'Recursive Fibonacci: {r_fib(6)}')