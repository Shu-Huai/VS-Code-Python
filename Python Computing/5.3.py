def CountCharacters(string):
    capitalLetter = 0
    smallLetter = 0
    number = 0
    otherCharacter = 0
    for character in string:
        if "A" <= character <= "Z":
            capitalLetter += 1
        elif "a" <= character <= "z":
            smallLetter += 1
        elif "0" <= character <= "9":
            number += 1
        else:
            otherCharacter += 1
    return (capitalLetter, smallLetter, number, otherCharacter)


print(CountCharacters("This is 123."))