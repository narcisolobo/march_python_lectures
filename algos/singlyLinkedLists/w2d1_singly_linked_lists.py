# Singly Linked List
# Day 1

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # SLList: Add Front
    # Given a value, create a new node, add it to the front of the singly linked list, and return the modified singly linked list.

    def add_front(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        return self

    # SLList: Add Back
    # Given a value, create a new node, add it to the back of the singly linked list, and return the modified singly linked list.
    
    def add_back(self, val):
        new_tail = Node(val)
        runner = self.head

        if runner == None:
            self.head = new_tail
        else:
            while(runner.next):
                runner = runner.next
            runner.next = new_tail
        return self;

    # Helper method. Returns a boolean.
    
    def isEmpty(self):
        return self.head == None

    # SLList: Print Vals
    # Create a function that prints all values in a singly linked list.
    
    def print_vals(self):
        if self.isEmpty():
            print("This SLL is empty.")
            return self
        else:
            runner = self.head
            output = f'**********\n'
            while (runner):
                output += f'{str(runner.val)} > '
                runner = runner.next
            print(output) 
        return self

    # SLList: Contains
    # Given a value, return true if that value is found in any node in the singly linked list. Return false if it is not.
    
    def contains(self,val):
        if self.isEmpty():
            print("This SLL is empty.")
            return self
        else:
            runner = self.head
            while (runner):
                if (runner.val == val):
                    print('True')
                    return True
                runner = runner.next
            print('False')
            return False