// SLList: Move Max to Back
// Create a function that moves the node with the maximum value to the tail of a singly linked list.
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

    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.addFront(temp);
        }
        return this;
    }

    addFront(val) {
        const newHead = new Node(val);
        newHead.next = this.head;
        this.head = newHead;
        return this;
    }

    isEmpty() {
        return this.head === null;
    }

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

    // SLList: Move Min to Front
    // Create a function that moves the node with the minimum value to the front of a singly linked list.

    minToFront() {
        // First, check if the list is empty.
        if (this.isEmpty()) {
            console.log('This SLL is empty.');
            return this;

        } else {
            // Set your variables
            let minNode = this.head;
            let runner = this.head;
            let prevNode = this.head;

            // Find and set the minNode.
            while (runner) {
                if (runner.val < minNode.val) {
                    minNode = runner;
                }
                runner = runner.next;
            }
            // Just printing out the minNode val to confirm.
            console.log(`The minNode val is: ${minNode.val}`)

            // If the minNode was already at the beginning, we're done.
            if (minNode === this.head) {
                return this;
            }

            // If not, set your runner at the head again.
            runner = this.head;

            // Go to the minNode
            while (runner !== minNode) {
                prevNode = runner;
                runner = runner.next;
            }

            // Remove the minNode
            prevNode.next = minNode.next;
            // Set the old head to minNode.next
            minNode.next = this.head;
            // Set the head to minNode
            this.head = minNode;
        }
        return this;
    }

    maxToBack() {
        // First, check if the SLL is empty.
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } else {
            // If the list isn't empty, find the maxNode.
            let maxNode = this.head;
            let runner = this.head;

            while (runner) {
                if (runner.val > maxNode.val) {
                    maxNode = runner;
                }
                runner = runner.next;
            }

            // Just printing the val of maxNode to confirm.
            console.log(`The maxNode val is: ${maxNode.val}`);

            // If maxNode is head, snip it out.
            if (maxNode === this.head) {
                this.head = this.head.next;
                runner = this.head;

                // Run to the end node.
                while (runner.next) {
                    runner = runner.next;
                }

                // Set next of last node to maxNode.
                runner.next = maxNode;
                // Set next of maxNode to null.
                maxNode.next = null;
            }

            // If it's already the tail, we're done.
            else if (maxNode.next === null) {
                return this;
            }

            // If it's not the head or the tail.
            else {
                runner = this.head;

                // Run to the end.
                while (runner.next) {
                    // But stop at maxNode on the way.
                    if (runner.next === maxNode) {
                        // Snip maxNode out.
                        runner.next = maxNode.next;
                    }
                    runner = runner.next;
                }
                // Set next of last node to maxNode.
                runner.next = maxNode;
                maxNode.next = null;
            }

        }
        return this;
    }
}

let mySLL = new SinglyLinkedList();
mySLL.populateRandom(200, 20).printVals();
mySLL.maxToBack().printVals();