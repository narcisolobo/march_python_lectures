// Reverse String
// Create a function reverseString(str) that, given a string, will return a string of the same length but with characters reversed. Example: given "creature", return "erutaerc". Do not use the built-in reverse() function!

function reverseString(str){
    let reversed = ''
    for (let i = str.length-1; i >= 0; i--){
        reversed += str[i]
    }
    return reversed
}

console.log(reverseString('Welcome to Python!'))