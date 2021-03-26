import random

class Arr_Stack:
    def __init__(self, items = []):
        self.items = items

    # ArrStack: Push
    # Create push(val) that adds val to our stack.
    def push(self, item):
        self.items.append(item)
        return self

    def populate_random(self, max, length):
        for i in range(length):
            temp = random.randint(1, max)
            self.push(temp)
        return self

    # ArrStack: Pop
    # Create pop() to remove and return the top val.
    def pop(self):
        return self.items.pop()

    # ArrStack: Top/Peek
    # Return (not remove) the stack’s top value.
    def peek(self):
        print(f'Top value is: {self.items[len(self.items) - 1]}')
        return self.items[len(self.items) - 1]

    # ArrStack: Is Empty
    # Return whether the stack is empty.
    def is_empty(self):
        return len(self.items) == 0

    # ArrStack: Size
    # Return the number of stacked values.
    def size(self):
        print(f'Size is: {len(self.items)}')
        return len(self.items)

    # ArrStack: Print Values
    # Print all values in the stack.
    def print_vals(self):
        print(self.items)
        return self

    # ArrStack: Contains
    # Return whether given val is within the stack.
    def contains(self, val):
        for i in range(len(self.items)):
            if(self.items[i] == val):
                print(f'Value ({val}) found.')
                return True
        print(f'Value ({val}) not found.')
        return False

my_arr_stack = Arr_Stack()
my_arr_stack.populate_random(300, 10).print_vals().contains(356)