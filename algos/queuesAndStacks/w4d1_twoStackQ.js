// Two Stack Queue:
// Using only two stack objects for the underlying data storage, recreate a Queue class.

// Remember, queues are first in, first out (FIFO) and stacks are last in, first out (LIFO).
// Assume there is no limit to the amount of values this two stack queue can hold.

class twoStackQ {
    constructor() {
        // The two stack objects will be arrays.
        // Consider stack1[stack1.length-1] to be the front of the queue.
        this.stack1 = [];
        this.stack2 = [];
    }

    // Two Stack Queue: Is Empty
    // Create class method isEmpty() to return true if the queue is empty.
    isEmpty() {
        return this.stack1.length === 0;
    }

    // Two Stack Queue: Enqueue
    // Create class method enqueue(val) to add a value to the queue.
    enqueue(val) {
        // Move all values from stack one to stack two.
        while (this.stack1.length !== 0) {
            this.stack2.push(this.stack1[this.stack1.length-1]);
            this.stack1.pop();
        }
        // Add val to stack one.
        this.stack1.push(val);
        
        // Move all values back to stack one from stack two.
        while(this.stack2.length !== 0) {
            this.stack1.push(this.stack2[this.stack2.length-1]);
            this.stack2.pop()
        }
        return this;
    }

    // Two Stack Queue: Dequeue
    // Create class method dequeue(val) to remove and return the first value from the queue.
    dequeue() {
        if(this.isEmpty()) {
            console.log('This two stack queue is empty.');
            return null;
        } else {
            console.log(this.stack1[this.stack1.length-1])
            return this.stack1.pop()
        }
    }
    
    // Two Stack Queue: Peek/Front
    // Create class method peek() to return (not remove) the first value in the queue.
    peek() {
        if(this.isEmpty()) {
            console.log('This two stack queue is empty.');
        } else {
            console.log(`Here is your peek: ${this.stack1[this.stack1.length-1]}`);
            return this.stack1[this.stack1.length-1];
        }
    }
    
    // Two Stack Queue: Print Values
    // Create class method printVals() to log all values in the queue to the console starting with the front.
    printVals() {
        if(this.isEmpty()) {
            console.log('This two stack queue is empty.');
            return this;
        } else {
            let output = '';
            for (let i = this.stack1.length-1; i >= 0; i--) {
                output += this.stack1[i].toString();
                output += ' > ';
            }
            console.log(output);
        }
        return this;
    }

    // Two Stack Queue: Contains
    // Create class method contains(val) to return true if val is in the queue and false if it is not.
    contains(val) {
        if(this.isEmpty()) {
            console.log('This two stack queue is empty.');
            return false;
        } else {
            for(let i = this.stack1.length-1; i >=0; i--) {
                if (this.stack1[i] === val) {
                    console.log(`Value (${val}) found.`);
                    return true;
                }
            }
            console.log(`Value (${val}) not found.`);
            return false;
        }
    }
    
    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.enqueue(temp)
        }
        return this;
    }
}