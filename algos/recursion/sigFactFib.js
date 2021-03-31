// Recursive Functions
// 1. Base Case
// 2. Forward Progress
// 3. Calling Back Into Itself

// Recursive Sigma
// Write a recursive function that takes in an integer and returns the sum of all previous integers.

// First, a linear solution:
function sigma(num) {
    let sum = 0;
    for (let i = 1; i <= num; i++) {
        sum += i;
    }
    return sum;
}
console.log(`Linear sigma: ${sigma(6)}`);

// Now, a recursive solution:
function rSigma(num) {
    if (num < 1) {
        return 0;
    } else {
        return num + rSigma(num - 1);
    }
}
console.log(`Recursive sigma: ${rSigma(6)}`);

// Recursive Factorial
// Write a recursive function that takes in an integer and returns the product of all previous integers.

// First, a linear solution:
function facto(num) {
    let product = 1;
    for (let i = 1; i <= num; i++) {
        product *= i;
    }
    return product;
}
console.log(`Linear factorial: ${facto(6)}`);

// Now, a recursive solution:
function rFacto(num) {
    if (num == 1) {
        return 1;
    } else {
        return num * rFacto(num - 1);
    }
}
console.log(`Recursive factorial: ${rFacto(6)}`);

// Recursive Fibonacci
// Write a recursive function that takes in an index and returns the value of a Fibonacci sequence at that index.

// First, a linear solution:
function fib(idx) {
    let sequence = [0, 1];
    for (let i = 2; i <= idx; i++) {
        sequence.push(sequence[i - 1] + sequence[i - 2]);
    }
    return sequence[idx];
}
console.log(`Linear Fibonacci: ${fib(6)}`);

// Now, a recursive solution:
function rFib(idx) {
    if (idx < 2) {
        return idx;
    } else {
        return rFib(idx - 1) + rFib(idx - 2);
    }
}
console.log(`Recursive Fibonacci: ${rFib(6)}`)