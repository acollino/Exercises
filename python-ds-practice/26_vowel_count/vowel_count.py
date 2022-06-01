def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_phrase = {}
    for letter in phrase:
        if(letter.isalpha() and vowels.count(letter.lower()) > 0):
            vowel = letter.lower()
            vowel_amount = vowels_in_phrase.get(vowel, -1)
            if vowel_amount == -1:
                vowels_in_phrase.update({vowel: 1})
            else:
                vowels_in_phrase.update({vowel: vowel_amount + 1})
    return vowels_in_phrase