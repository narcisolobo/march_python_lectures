class ArrStack {
    constructor(items = []) {
        this.items = items;
    }

    // ArrStack: Push
    // Create push(val) that adds val to our stack.
    push(item) {
        this.items.push(item);
        return this;
    }

    populateRandom(max, length) {
        for (let i = 1; i <= length; i++) {
            let temp = Math.floor(Math.random() * max) + 1;
            this.push(temp);
        }
        return this;
    }

    // ArrStack: Pop
    // Create pop() to remove and return the top val.
    pop() {
        return this.items.pop();
    }

    // ArrStack: Top/Peek
    // Return (not remove) the stack’s top value.
    peek() {
        return this.items[this.items.length - 1];
    }

    // ArrStack: Is Empty
    // Return whether the stack is empty.
    isEmpty() {
        return this.items.length === 0;
    }

    // ArrStack: Size
    // Return the number of stacked values.
    size() {
        return this.items.length;
    }

    // ArrStack: Print Values
    // Print all values in the stack.
    printVals() {
        let output = '[';
        output += this.items.join(', ');
        output += ']';
        console.log(output);
        return this;
    }

    // ArrStack: Contains
    // Return whether given val is within the stack.
    contains(val) {
        for (let i = 0; i < this.items.length; i++){
            if(this.items[i] === val) {
                console.log(`Value (${val}) found.`);
                return true;
            }
        }
        console.log(`Value (${val}) not found.`);
        return false;
    }
}