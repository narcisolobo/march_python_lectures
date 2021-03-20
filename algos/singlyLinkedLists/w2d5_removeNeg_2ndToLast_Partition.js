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

    isEmpty() {
        return this.head === null;
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

    contains(val) {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
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

    // SLList: Remove Negatives
    // Create a function that removes all negative values from a list, then return the modified list.
    removeNegatives() {
        let prev = null;
        let runner = this.head;

        while (runner) {
            if(runner.val < 0) {
                if(prev === null) {
                    this.head = runner.next;
                } else {
                    prev.next = runner.next;
                }
            }
            prev = runner;
            runner = runner.next;
        }
        return this;
    }
    
    // Second to Last Value
    // Create a function that returns the value in the second-to-last node.
    secondToLastVal() {
        let runner = this.head;
        if(runner === null || runner.next == null) {
            console.log("This list does not contain enough nodes.")
            return this;
        } else {
            let prev = null;
            while(runner.next) {
                prev = runner;
                runner = runner.next;
            }
            console.log(`Second-to-last val: ${prev.val}`)
        }
        return this;
    }
    
    // Partition
    // Create a function that, given a value, locates the first node with that value, moves all nodes with values less than that value to be earlier, and moves all nodes with values greater than that value to be later. Otherwise, original order need not be perfectly preserved. Return the list when complete.
    partition(val) {
        if (this.isEmpty()) {
            console.log("This SLL is empty.")
            return this;
        } else {
            if(!this.contains(val)) {
                return this;
            } else {
                let lowerList = new SinglyLinkedList();
                let higherList = new SinglyLinkedList();
                let valCount = 0;
                let runner = this.head;

                while(runner) {
                    if (runner.val < val) {
                        lowerList.addFront(runner.val);
                    } else if (runner.val > val) {
                        higherList.addFront(runner.val)
                    } else {
                        valCount++;
                    }
                    runner = runner.next
                }
                for (let i = 0; i < valCount; i++) {
                    higherList.addFront(val);
                }
                runner = lowerList.head;
                while(runner.next){
                    runner = runner.next;
                }
                runner.next = higherList.head;
                this.head = lowerList.head;
            }
        }
        return this;
    }
}