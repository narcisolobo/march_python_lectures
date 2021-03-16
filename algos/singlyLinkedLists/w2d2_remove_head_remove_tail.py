# Day 2
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    # My populateRandom method uses add_back, so I'd better paste it here.
    # addFront would have been a more efficient choice in hindsight.
    def add_back(self, val):
        new_tail = Node(val)
        runner = self.head

        if(runner == None):
            self.head = new_tail
        else:
            while(runner.next):
                runner = runner.next
            runner.next = new_tail
        return self

    # Populates a list of <length> with nodes containing values between one and <max>.
    def populate_random(self, max, length):
        for i in range(length):
            temp = random.randrange(1, max)
            self.add_back(temp)
        return self

    # Edge case helper method.
    def is_empty(self):
        return self.head == None

    # Printing values of each node with a little greater than symbol to visualize the .next property.
    def print_vals(self):
        if (self.is_empty()):
            print("This SLL is empty.")
            return self
        else:
            runner = self.head
            output = '**********\n'
            while (runner):
                output += f'{str(runner.val)} > '
                runner = runner.next
            print(output)
        return self

    # SLList: Remove Head
    # Create a function that removes the head node from a singly linked list.
    def remove_head(self):
        if (self.is_empty()):
            print("This SLL is empty.")
            return self
        else:
            self.head = self.head.next
        return self
    
    # SLList: Remove Tail
    # Create a function that removes the tail node from a singly linked list.
    def remove_tail(self):
        if (self.is_empty()):
            print("This SLL is empty.")
            return self
        else:
            previous = self.head
            runner = self.head
            while (runner.next):
                previous = runner
                runner = runner.next
            previous.next = None
        return self

mySLL = Singly_Linked_List()
mySLL.populate_random(200, 20).print_vals()
mySLL.remove_tail().print_vals()