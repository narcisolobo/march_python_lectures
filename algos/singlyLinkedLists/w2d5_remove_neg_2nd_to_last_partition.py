import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def populate_random(self, max, length):
        for i in range(length):
            temp = random.randrange(1, max)
            self.add_front(temp)
        return self

    def add_front(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        return self

    def contains(self, val):
        if (self.is_empty()):
            print("This SLL is empty.")
            return self
        else:
            runner = self.head
            while (runner):
                if (runner.val == val):
                    print(f'Value ({val}) found.')
                    return True
                runner = runner.next
            print(f'Value ({val}) not found.')
            return False

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

    # SLList: Remove Negatives
    # Create a function that removes all negative values from a list, then return the modified list.
    def remove_negatives(self):
        prev = None
        runner = self.head

        while (runner):
            if(runner.val < 0):
                if(prev == None):
                    self.head = runner.next
                else:
                    prev.next = runner.next
            prev = runner
            runner = runner.next
        return self
    
    # Second to Last Value
    # Create a function that returns the value in the second-to-last node.
    def second_to_last_val(self):
        runner = self.head
        if(runner == None or runner.next == None):
            print("This list does not contain enough nodes.")
            return self
        else:
            prev = None
            while(runner.next):
                prev = runner
                runner = runner.next
            print(f'Second-to-last val: {prev.val}')
        return self
    
    # Partition
    # Create a function that, given a value, locates the first node with that value, moves all nodes with values less than that value to be earlier, and moves all nodes with values greater than that value to be later. Otherwise, original order need not be perfectly preserved. Return the list when complete.
    def partition(self, val):
        if (self.is_empty()):
            print("This SLL is empty.")
            return self
        else:
            if(not self.contains(val)):
                return self
            else:
                lowerList = Singly_Linked_List()
                higherList = Singly_Linked_List()
                valCount = 0
                runner = self.head

                while(runner):
                    if (runner.val < val):
                        lowerList.add_front(runner.val)
                    elif (runner.val > val):
                        higherList.add_front(runner.val)
                    else:
                        valCount += 1
                    runner = runner.next
                for i in range(valCount):
                    higherList.add_front(val)
                runner = lowerList.head
                while(runner.next):
                    runner = runner.next
                runner.next = higherList.head
                self.head = lowerList.head
        return self

mySLL = Singly_Linked_List()
mySLL.populate_random(300, 10).add_front(150).populate_random(300, 10).print_vals()
mySLL.partition(150).print_vals()