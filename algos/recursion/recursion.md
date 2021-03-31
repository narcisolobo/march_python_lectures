# Recursion and Dynamic Programming.
Recursion occurs when a function calls itself. Dynamic programming is more general: breaking large problems into smaller, more solvable ones.

Let's consider an example: "I'm thinking of an integer between 1 and 120. Guess it." If you were to guess '61', and I said "nope, that's too high," then how would you respond? You would treat this exactly as if we had just started and I had said "I'm thinking of an integer between 1 and 60." In doing this, you reframed the problem as a less complex one, a technique called dynamic programming.

Let us continue: if next you guessed '30', and I said "nope, too low," then you could again reframe the problem as "I'm thinking of a number from 31 to 60." Let's say you then guessed '42', to which I said "Yes, you guessed it! How did you know that was the answer?" With this 'divide- and-conquer' approach, you could guess the correct number in a 1-120 range, in just 6 guesses on average.

## Three Requirements For Effective Recursion

1. Base case:
    - When a function can determine (and return) an answer immediately, this is a 'base case'. If you successfully guess my number, I know right away that the game is over. Conversely, if you search for 'spizzwink' in an alphabetized word list and find nothing between 'spitz' and 'splash', you need not continue: 'spizzwink' was not found. There are positive and negative base cases.

2. Forward progress:
    - When a function cannot solve a problem but can narrow the range of possibilities, this is 'forward progress'. Learning that '61' is too high, you have made forward progress because you now know the solution is outside the '61-120' range. For recursion to be effective, you must make at least a little forward progress in every possible case. If there is a case in which you can neither solve the problem nor break it down further, then your solution is not complete.

3. Calling back into itself as if it were the original problem:
    - If my initial challenge were "I'm thinking of an integer between 1 and 60", you would proceed just as you did in originally after your first guess. If "taking a guess" is a function call, this function wouldn't know the difference between initial and subsequent calls. A recursive function calls itself to narrow things down, but like most functions it generally does not need to know anything about its caller – the fact that the caller might be itself is not an important distinction.

When creating (and debugging) recursive code, remember: each function call creates a new stack frame (essentially, a new T-diagram). Call stack space is limited, so recurse with care.