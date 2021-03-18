// Day 4

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

    addFront(val) {
        const newHead = new Node(val);
        newHead.next = this.head;
        this.head = newHead;
        return this;
    }

    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.addFront(temp);
        }
        return this;
    }

    isEmpty() {
        return this.head === null;
    }

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

    // SLList: Prepend Value
    // Given a value and a target value, create a node containing value and insert it before the node containing the target value in a singly linked list.

    prependVal(val, target) {

        // First, check if the list is empty. 
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } 

        // Next, check if the target value is in the list.
        else if (!this.contains(target)) {
            return this;
        } else {

            // Create the new node and set runner to head node.
            const newNode = new Node(val);
            let runner = this.head;
            
            // Run along list and land in front of target node.
            while (runner.next.val != target) {
                runner = runner.next;
            }

            // Put newNode after runner (before target node).
            newNode.next = runner.next;
            runner.next = newNode;
            return this;
        }
    }

    // SLList: Append Value
    // Given a value and a target value, create a node containing value and insert it after the node containing the target value in a singly linked list.

    appendVal(val, target) {

        // First, check if the list is empty. 
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } 

        // Next, check if the target value is in the list.
        else if (!this.contains(target)) {
            return this;
        } else {

            // Create the new node and set runner to head node.
            const newNode = new Node(val);
            let runner = this.head;
            
            // Run along list and land on target node.
            while (runner.val != target) {
                runner = runner.next;
            }

            // Put newNode in-between runner and target node.
            newNode.next = runner.next;
            runner.next = newNode;
            return this;
        }
    }
}

let mySLL = new SinglyLinkedList()
mySLL.populateRandom(100, 10).addFront(2).populateRandom(100, 10).appendVal(20, 2).printVals()