// Create Queue Using Two Stacks
// Using only two Stack objects for the underlying data storage, recreate a Queue class.

class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SLQueue {
    constructor() {
        this.head = null;
        this.tail = null;
    }
}

class SLQueue2St {
    constructor(stack1, stack2) {
        this.stack1 = stack1;
        this.stack2 = stack2;
    }
}