// Parens Valid
// Create a function that, given an input string, returns a boolean whether parentheses in that string are valid. Given input "y(3(p)p(3)r)s", return true. Given "n(0(p)3", return false. Given "n)0(t(0)k", return false.

function parensValid(str) {
    const parensStack = [];

    for (const char of str) {
        if (char === "(") {
            parensStack.push(char);
        }
        else if (char === ")") {
            if (parensStack.length === 0) {
                return false;
            } else {
                parensStack.pop();
            }
        }
    }
    return parensStack.length === 0;
}