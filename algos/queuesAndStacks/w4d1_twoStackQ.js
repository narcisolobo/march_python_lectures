// Two Stack Queue:
// Using only two stack objects for the underlying data storage, recreate a Queue class.

// Remember, queues are first in, first out (FIFO) and stacks are last in, last out (LIFO).
// Assume there is no limit to the amount of values this two stack queue can hold.

class twoStackQ {
    constructor() {
        // The two stack objects will be arrays.
        // Consider stack1.length-1 to be the front of the queue.
        this.stack1 = [];
        this.stack2 = [];
    }

    // Two Stack Queue: Is Empty
    // Create class method isEmpty() to return true if the queue is empty.
    isEmpty() {
        // Your code here.
    }

    // Two Stack Queue: Enqueue
    // Create class method enqueue(val) to add a value to the queue.
    // Move all values from stack one to stack two.
    // Add val to stack one.
    // Move all values back to stack one from stack two.
    // Consider writing a populateRandom() method that calls enqueue(val) to quickly populate your queue.
    
    enqueue(val) {
        // Your code here.
        return this;
    }

    // Two Stack Queue: Dequeue
    // Create class method dequeue(val) to remove and return the first value from the queue.
    dequeue() {
        // Your code here.
    }
    
    // Two Stack Queue: Peek/Front
    // Create class method peek() to return (not remove) the first value in the queue.
    peek() {
        // Your code here.
    }
    
    // Two Stack Queue: Print Values
    // Create class method printVals() to log all values in the queue to the console starting with the front.
    printVals() {
        // Your code here.
        return this;
    }

    // Two Stack Queue: Contains
    // Create class method contains(val) to return true if val is in the queue and false if it is not.
    contains(val) {
        // Your code here.
    }
}