# Day 3
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

    # SLList: Move Min to Front
    # Create a function that moves the node with the minimum value to the front of a singly linked list.

    def min_to_front(self):
        # First, check if the list is empty.
        if (self.is_empty()):
            print('This SLL is empty.')
            return self

        else:
            # Set your variables
            minNode = self.head
            runner = self.head
            prevNode = self.head

            # Find and set the minNode.
            while (runner):
                if (runner.val < minNode.val):
                    minNode = runner
                runner = runner.next

            # Just printing out the minNode val to confirm.
            print(f'The minNode val is: {minNode.val}')

            # If the minNode was already at the beginning, we're done.
            if (minNode == self.head):
                return self

            # If not, set your runner at the head again.
            runner = self.head

            # Go to the minNode
            while (runner != minNode):
                prevNode = runner
                runner = runner.next
    

            # Remove the minNode
            prevNode.next = minNode.next
            # Set the old head to minNode.next
            minNode.next = self.head
            # Set the head to minNode
            self.head = minNode

        return self

    def max_to_back(self):
        # First, check if the SLL is empty.
        if (self.is_empty()):
            print("This SLL is empty.")
            return self
        else:
            # If the list isn't empty, find the max_node.
            max_node = self.head
            runner = self.head

            while (runner):
                if (runner.val > max_node.val):
                    max_node = runner
                runner = runner.next

            # Just printing the val of max_node to confirm.
            print(f'The max_node val is: {max_node.val}')

            # If max_node is head, snip it out.
            if (max_node == self.head):
                self.head = self.head.next
                runner = self.head

                # Run to the end node.
                while (runner.next):
                    runner = runner.next

                # Set next of last node to max_node.
                runner.next = max_node
                # Set next of max_node to None.
                max_node.next = None

            # If it's already the tail, we're done.
            elif (max_node.next == None):
                return self

            # If it's not the head or the tail.
            else:
                runner = self.head

                # Run to the end.
                while (runner.next):
                    # But stop at max_node on the way.
                    if (runner.next == max_node):
                        # Snip max_node out.
                        runner.next = max_node.next

                    runner = runner.next

                # Set next of last node to max_node.
                runner.next = max_node
                max_node.next = None

        return self

mySLL = Singly_Linked_List()
mySLL.populate_random(200, 20).print_vals()
mySLL.max_to_back().print_vals()