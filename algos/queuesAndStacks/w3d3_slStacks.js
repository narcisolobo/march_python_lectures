// Singly Linked List Stack (LIFO)
// You can treat the back of the linked list as the top of the stack, adding to it and removing from the back to maintain LIFO But it's more efficient to add to the front and remove from the front, which is still LIFO.

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SLStack {
    constructor() {
        this.head = null;
    }

    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.push(temp);
        }
        return this;
    }

    // push(val) {
    // push val to top of stack
    push(val) {
        const newNode = new Node(val);
        if (this.head === null) {
            this.head = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        return this;
    }

    // pop() {
    // remove and return val at top of stack
    pop() {
        if (this.head === null) {
            return null;
        } else {
            const removed = this.head;
            this.head = this.head.next;
            console.log(`Value popped: ${removed.val}`)
            return removed.val;
        }
    }

    // peek() {
    // return val at top of stack without removing
    peek() {
        if (this.head === null) {
            return null;
        } else {
            console.log(`Here's your peek: ${this.head.val}`)
            return this.head.val;
        }
    }

    // contains(val) {
    // return true if SLStack contains value
    // return false if SLStack does not contain value
    contains(val) {
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

    // isEmpty() {
    // return true if SLStack is empty
    // return false if SLStack is not empty
    isEmpty() {
        return this.head === null;
    }

    // size() {
    // return length of SLStack
    size() {
        let len = 0;
        let runner = this.head;

        while (runner) {
            len += 1;
            runner = runner.next;
        }
        console.log(`Size is ${len}`)
        return len;
    }

    // printVals() {
    // print out the values of the SLStack
    printVals() {
        if (this.isEmpty()) {
            console.log('Queue is empty.')
            return this;
        } else {
            let runner = this.head;
            let output = `**********\n`
            while (runner) {
                output += `${runner.val.toString()} > `;
                runner = runner.next;
            }
            console.log(output);
        }
        return this;
    }
}

let myslStack = new SLStack()
myslStack.populateRandom(300, 10).printVals().size()