// Singly Linked List
// Day 1

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

    // SLList: Add Front
    // Given a value, create a new node, add it to the front of the singly linked list, and return the modified singly linked list.

    addFront(val) {
        const newHead = new Node(val);
        newHead.next = this.head;
        this.head = newHead;
        return this;
    }

    // SLList: Add Back
    // Given a value, create a new node, add it to the back of the singly linked list, and return the modified singly linked list.

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

    // Helper method. Returns a boolean.

    isEmpty() {
        return this.head === null;
    }

    // SLList: Print Vals
    // Create a function that prints all values in a singly linked list.

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

    // SLList: Contains
    // Given a value, return true if that value is found in any node in the singly linked list. Return false if it is not.

    contains(val) {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } else {
            let runner = this.head;
            while (runner) {
                if (runner.val === val) {
                    return true;
                }
                runner = runner.next;
            }
            return false;
        }
    }
}

let mySll = new SinglyLinkedList();
console.log(mySll);

mySll.addFront(5).addFront(7).addFront(6).addFront(8);
mySll.addBack(3).addBack(0).addBack(9).printVals();