def is_palindrome(stg):
    for i in range(int(len(stg)/2)):
        if stg[i] != stg[len(stg)-1-i]:
            return False
    return True

# function reverseString(str){
#     let reversed = '';
#     for (let i = str.length-1; i >= 0; i--){
#         reversed += str[i];
#     }
#     return reversed;
# }

# Let's import our reverse string from Monday!

from w1d1_reverse_string import reverse_string

def is_palindrome_dry(stg):
    temp = reverse_string(stg)
    if temp != stg:
        return False
    else:
        return True

print(is_palindrome_dry('racecar'))

# We now have DRY (Don't Repeat Yourself) code.