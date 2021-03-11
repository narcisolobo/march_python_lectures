# Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given "there's no free lunch - gotta pay yer way", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN".

# THIS CODE DOESN'T WORK

def acronymize(input_string):
    acronym = ''
    # just so I don't have to keep typing out len(input_string)
    length = len(input_string)
    input_string += ' '

    for i in range(length):
        # skip spaces, handles multiple spaces
        while i == ' ' and i < length:
            i += 1
            print(i)
        # change the character to uppercase
        acronym += input_string[i].upper()
        print(acronym)
        # skip the rest of the word
        while input_string[i] != ' ' and i < length:
            i += 1
            print(i)
    return acronym

print(acronymize("there's no free lunch - gotta pay yer way"))