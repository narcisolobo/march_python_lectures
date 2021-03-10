// Is Palindrome

// Strings like "Able was I, ere I saw Elba" or "Madam, I'm Adam" 
// could be considered palindromes, because (if we ignore spaces, punctuation and capitalization) 
// the letters are the same from front and back.

// Create a function that returns a boolean 
// whether the string is a strict palindrome. 
// For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: 
// if given "Dud" or "oho!", return false.

// function is_palidrome(){

// }

// is_palidrome("racecar") //returns true
// is_palidrome("madam") //returns true
// is_palidrome("oho") //returns true
// is_palidrome("bonkers") //returns false

// Below are some of the students' solutions. I missed the first one, sorry!

function isPalindromeMrHoller(str) {
    j = str.length - 1;
    for (let i = 0; i < j; i++) {
        if (str.charAt(i) != str.charAt(j)) {
            return false;
        } else {
            j--
        }
    }
    return true;

}

function isPalindromeMrOkoh(str){
    for (let i = 0; i < str.length/2; i++){
        if (str[i] !== str[str.length-1-i]){
            return false;
        }
    }
    return true;
}

// As Mr. Bludworth pointed out, we could have used our reverseString algorithm from Monday to help us out on this one.

function reverseString(str){
    let reversed = '';
    for (let i = str.length-1; i >= 0; i--){
        reversed += str[i];
    }
    return reversed;
}

// We could use this function to modularize our code. Like so:

function isPalindromeMrBludworth(str){
    const temp = reverseString(str);
    if (temp !== str){
        return false;
    } else {
        return true;
    }
}

// We now have DRY (Don't Repeat Yourself) code.