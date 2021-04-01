// Greatest Common Factor / Greatest Common Divisor
// The highest number that divides evenly into two or more numbers.

// 12, 8
// Factors of 12 = 1, 2, 3, 4, 6, 12
// Factors of 8 = 1, 2, 4, 8
// 4 is the highest number that divides evenly into 12 and 8.

// Euclid's Algorithm:
// Given two whole numbers where a is greater than b, do the division a ÷ b = c with remainder R.
// Replace a with b, replace b with R and repeat the division.
// Repeat step 2 until R=0.
// When R=0, the divisor, b, in the last equation is the greatest common factor, GCF.

// 12 % 8 = 4
// 8 % 4 = 0

// Recursive algorithm for Greatest Common Factor (GCF)
// Write a recursive function that takes in two integers and returns the greatest common factor.

// Remember, a recursive function should have:
// 1. Base Case
// 2. Forward Progress
// 3. A Call to the Function Inside the Function

function rGCF(a, b) {
    if (!b) {
        return a;
    } else {
        return rGCF(b, a % b);
    }
}

// Predicted call stack:
// rGCF(12, 81)
// rGCF(81, 12)
// rGCF(12, 9)
// rGCF(9, 3)
// rGCF(3, 0)
// 3 is the predicted GCF.

console.log(rGCF(15, 62))