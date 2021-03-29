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
        return len(self.stack1) == 0

    # Two Stack Queue: Enqueue
    # Create class method enqueue(self, val) to add a value to the queue.
    def enqueue(self, val):
        # Move all elements from stack1 to stack2 
        while len(self.stack1) != 0: 
            self.stack2.append(self.stack1[-1]) 
            self.stack1.pop()
        # Push item into self.stack1 
        self.stack1.append(val) 
        # Push everything back to stack1 
        while len(self.stack2) != 0: 
            self.stack1.append(self.stack2[-1]) 
            self.stack2.pop()
        return self

    # Two Stack Queue: Dequeue
    # Create class method dequeue(self, val) to remove and return the first value from the queue.
    def dequeue(self):
        # if first stack is empty 
        if self.is_empty():
            print('This two stack queue is empty.')
        else:
            # Return top of self.stack1 
            print(f'Popped: {self.stack1[-1]}')
            return self.stack1.pop()
    
    # Two Stack Queue: Peek/Front
    # Create class method peek(self) to return (not remove) the first value in the queue.
    def peek(self):
        if self.is_empty():
            print('This two stack queue is empty.')
        else:
            print(f'Here is your peek: {self.stack1[-1]}')
            return self.stack1[-1]

    # Two Stack Queue: Print Values
    # Create class method print_vals(self) to print all values in the queue starting with the front.
    def print_vals(self):
        if self.is_empty():
            print('This two stack queue is empty.')
        else:
            output = ''
            for i in range(len(self.stack1)-1, 0, -1):
                output += str(self.stack1[i])
                output += ' > '
            print(output)
            return self
    
    # Two Stack Queue: Contains
    # Create class method contains(self, val) to return true if val is in the queue and false if it is not.
    def contains(self, val):
        if self.is_empty():
            print('This two stack queue is empty.')
        else:
            for item in self.stack1:
                if item == val:
                    print(f'Value ({val}) found.')
                    return True
            print(f'Value ({val}) not found.')
            return False
    
    def populate_random(self, max, length):
        for i in range(length):
            temp = random.randint(1, max)
            self.enqueue(temp)
        return self