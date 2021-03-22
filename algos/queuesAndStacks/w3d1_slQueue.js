class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

// FIFO
// First In, First Out

class SLQueue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.enqueue(temp);
        }
        return this;
    }

    isEmpty() {
        return this.head === null;
    }

    printVals() {
        if (this.isEmpty()) {
            console.log('Queue is empty.')
            return this;
        } else {
            let runner = this.head;
            let output = '**********\n'
            while (runner) {
                output += `${runner.val.toString()} > `;
                runner = runner.next;
            }
            console.log(output);
        }
        return this;
    }

    // SLQueue: Enqueue
    // Create SLQueue method enqueue(val) to add the given value to end of our queue.
    enqueue(val) {
        const newTail = new Node(val);

        if (this.isEmpty()) {
            this.head = newTail;
            this.tail = newTail;

        } else {
            this.tail.next = newTail;
            this.tail = newTail;
        }

        this.size++;
        return this;
    }
    // SLQueue: Dequeue
    // Create SLQueue method dequeue() to remove and return the front value in the queue.
    dequeue() {
        if (this.isEmpty()) {
            console.log('Queue is empty.')
            return null;
        } else {
            // remove head and store it
            const dequeued = this.head;
            this.head = this.head.next;

            if (this.head === null) {
                this.tail = null;
            }

            this.size--;
            return dequeued.val;
        }
    }
    // SLQueue: Peek/Front
    // Create SLQueue method peek() to return the value at front of our queue, without removing it.
    peek() {
        if (this.isEmpty()) {
            console.log('Queue is empty.')
            return null;
        } else {
            console.log(`Peek: ${this.head.val}`)
            return this.head.val;
        }
    }

    // SLQueue: Contains
    // Create SLQueue method contains() to return true if the value is contained in the queue, and false if it is not.
    contains(val) {
        if (this.isEmpty()) {
            console.log('Queue is empty.')
            return null;
        } else {
            let runner = this.head;
            while (runner) {
                if (runner.val === val) {
                    console.log(`Value (${val}) found.`)
                    return true;
                }
                runner = runner.next;
            }
            console.log(`Value (${val}) not found.`)
            return false;
        }
    }

    // SLQueue: Return Size
    // Create SLQueue method getSize() to return the number of values in the queue.
    getSize() {
        console.log(this.size);
        return this.size;
    }
}