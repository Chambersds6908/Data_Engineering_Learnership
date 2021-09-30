def vowels(word):
    list_of_vowels = ""
    number_of_vowels = 0
    for letter in word:
        if letter in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]:
            if not letter in list_of_vowels:
                number_of_vowels += 1
                if number_of_vowels == 1:
                    list_of_vowels += letter.lower()
                else:
                    list_of_vowels += ", " + letter.lower()
    return "Vowels: " + list_of_vowels

vowels("Umuzi")