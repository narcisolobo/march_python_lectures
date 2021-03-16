// Day 2

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
    }

    // My populateRandom method uses addBack, so I'd better paste it here.
    // addFront would have been a more efficient choice in hindsight.
    addBack(val){
        const newTail = new Node(val);
        let runner = this.head;

        if(runner === null){
            this.head = newTail
        } else {
            while(runner.next) {
                runner = runner.next;
            }
            runner.next = newTail;
        }
        return this;
    }

    // Populates a list of <length> with nodes containing values between one and <max>.
    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.addBack(temp);
        }
        return this;
    }

    // Edge case helper method.
    isEmpty() {
        return this.head === null;
    }

    // Printing values of each node with a little greater than symbol to visualize the .next property.
    printVals() {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
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

    // SLList: Remove Head
    // Create a function that removes the head node from a singly linked list.
    removeHead() {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } else {
            this.head = this.head.next;
        }
        return this;
    }
    
    // SLList: Remove Tail
    // Create a function that removes the tail node from a singly linked list.
    removeTail() {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } else {
            let previous = this.head;
            let runner = this.head;

            while (runner.next) {
                previous = runner;
                runner = runner.next;
            }

            previous.next = null;
        }

        return this;
    }
}

let mySLL = new SinglyLinkedList()
mySLL.populateRandom(200, 20).printVals()
mySLL.removeTail().printVals()