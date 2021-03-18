import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    # My populateRandom method uses add_front, so I'd better paste it here.
    def add_front(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        return self
    
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
            self.add_front(temp)
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
    
    # SLList: Prepend Value
    # Given a value and a target value, create a node containing value and insert it before the node containing the target value in a singly linked list.

    def prepend_val(self, val, target):
        new_node = Node(val)
        runner = self.head

        while (runner.next.val != target):
            runner = runner.next
        new_node.next = runner.next
        runner.next = new_node

        return self

    # SLList: Append Value
    # Given a value and a target value, create a node containing value and insert it after the node containing the target value in a singly linked list.

    def append_val(self, val, target):
        new_node = Node(val)
        runner = self.head

        while (runner.val != target):
            runner = runner.next
        new_node.next = runner.next
        runner.next = new_node

        return self