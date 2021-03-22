import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# FIFO
# First In, First Out

class SLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def populate_random(self, max, length):
        for i in range(length):
            temp = random.randint(1, max)
            self.enqueue(temp)
        return self

    def is_empty(self):
        return self.head == None

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

    # SLQueue: Enqueue
    # Create SLQueue method enqueue(val) to add the given value to end of our queue.
    def enqueue(self, val):
        new_tail = Node(val)

        if (self.is_empty()):
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail

        self.size += 1
        return self

    # SLQueue: Dequeue
    # Create SLQueue method dequeue() to remove and return the front value in the queue.
    def dequeue(self):
        if (self.is_empty()):
            print(f'Queue is empty.')
            return None
        else:
            # remove head and store it
            dequeued = self.head
            self.head = self.head.next

            if (self.head == None):
                self.tail = None

            self.size -= 1
            print(f'Dequeued val: {dequeued.val}')
            return dequeued.val

    # SLQueue: Peek/Front
    # Create SLQueue method peek() to return the value at front of our queue, without removing it.
    def peek(self):
        if (self.is_empty()):
            print(f'Queue is empty.')
            return None
        else:
            print(f'Peek: {self.head.val}')
            return self.head.val

    # SLQueue: Contains
    # Create SLQueue method contains() to return True if the value is contained in the queue, and False if it is not.
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

    # SLQueue: Return Size
    # Create SLQueue method get_size() to return the number of values in the queue.
    def get_size(self):
        print(self.size)
        return self.size

mySLQ = SLQueue()
mySLQ.populate_random(300, 10).enqueue(34).populate_random(300, 10).print_vals().contains(34)