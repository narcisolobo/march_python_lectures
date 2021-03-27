# Two Stack Queue:
# Using only two stack objects for the underlying data storage, recreate a Queue class.

# Remember, queues are first in, first out (FIFO) and stacks are last in, last out (LIFO).
# Assume there is no limit to the amount of values this two stack queue can hold.

class two_stackq: 
    def __init__(self):
        # The two stack objects will be lists.
        # Consider stack1[-1] to be the front of the queue.
        self.stack1 = []
        self.stack2 = []
    
    # Two Stack Queue: Is Empty
    # Create class method is_empty(self) to return true if the queue is empty.
    def is_empty(self):
        # Your code here

    # Two Stack Queue: Enqueue
    # Create class method enqueue(self, val) to add a value to the queue.

    # PSEUDOCODE
    # Move all values from stack one to stack two.
    # Add val to stack one.
    # Move all values back to stack one from stack two.
    # Consider writing a populate_random(self) method that calls enqueue(self, val) to quickly populate your queue.
    def enqueue(self, val):
        # Your code here.
        return self

    # Two Stack Queue: Dequeue
    # Create class method dequeue(self, val) to remove and return the first value from the queue.
    def dequeue(self):
        # Your code here.
    
    # Two Stack Queue: Peek/Front
    # Create class method peek(self) to return (not remove) the first value in the queue.
    def peek(self):
        # Your code here.

    # Two Stack Queue: Print Values
    # Create class method print_vals(self) to print all values in the queue starting with the front.
    def print_vals(self):
        # Your code here.
        return self
    
    # Two Stack Queue: Contains
    # Create class method contains(self, val) to return true if val is in the queue and false if it is not.
    def contains(self, val):
        # Your code here.