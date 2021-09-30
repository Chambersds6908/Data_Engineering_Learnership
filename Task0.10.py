def common_letters(word1,word2):
    list_of_common_letters = ""
    number_of_common_letters = 0
    for letter in word1:
        if letter in word2:
            if not letter in list_of_common_letters:
                number_of_common_letters += 1
                if number_of_common_letters == 1:
                    list_of_common_letters += letter
                else:
                    list_of_common_letters += ", " + letter
    return "Common letters: " + list_of_common_letters

common_letters("wanted", "alive")