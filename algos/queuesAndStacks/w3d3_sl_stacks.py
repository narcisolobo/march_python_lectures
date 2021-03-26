# Singly Linked List Stack (LIFO)
# You can treat the back of the linked list as the top of the stack, adding to it and removing from the back to maintain LIFO But it's more efficient to add to the front and remove from the front, which is still LIFO.

import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLStack:
    def __init__(self):
        self.head = None

    def populate_random(self, max, length):
        for i in range(length):
            temp = random.randint(1, max)
            self.push(temp)
        return self

    # push(val):
    # push val to top of stack
    def push(self, val):
        new_node = Node(val)
        if (self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            return self

    # pop():
    # remove and return val at top of stack
    def pop(self):
        if (self.head == None):
            return None
        else:
            removed = self.head
            self.head = self.head.next
            return removed.val

    # peek():
    # return val at top of stack without removing
    def peek(self):
        if (self.head == None):
            print('This stack is empty.')
            return None
        else:
            print(f'Your peek: {self.head.val}')
            return self.head.val
    
    # contains(val):
    # return true if SLStack contains value
    # return false if SLStack does not contain value
    def contains(self, val):
        if (self.is_empty()):
            print(f'Queue is empty.')
            return None
        else:
            runner = self.head
            while (runner):
                if (runner.val == val):
                    print(f'Value ({val}) found.')
                    return True
                runner = runner.next
            print(f'Value ({val}) not found.')
            return False

    # isEmpty():
    # return true if SLStack is empty
    # return false if SLStack is not empty
    def is_empty(self):
        return self.head == None

    # size():
    # return length of SLStack
    def size(self):
        length = 0
        runner = self.head
        while (runner):
            length += 1
            runner = runner.next
        print(f'Number of nodes: {length}')
        return length

    # printVals():
    # print out the values of the SLStack
    def print_vals(self):
        if (self.is_empty()):
            print('This queue is empty.')
            return self
        else:
            runner = self.head
            output = '**********\n'
            while (runner):
                output += f'{str(runner.val)} > '
                runner = runner.next
            print(output)
        return self

my_sl_stack = SLStack()
my_sl_stack.populate_random(300, 10).push(150).print_vals().size()