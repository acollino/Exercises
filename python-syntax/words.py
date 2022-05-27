"""
For a list of words, print out each word on a separate line, 
but in all uppercase. Do this as a function, print_upper_words.
(Don't forget to add a docstring to your function!)

Change that function so that it only prints words that start with
the letter 'e' (either upper or lowercase).

Make your function more general: you should be able to pass in a 
set of letters, and it only prints words that start with one of 
those letters.
"""


def print_upper_words(word_list):
    """
    Given a list of strings, convert each string to uppercase and
    print each string on a separate line.
    """
    for word in word_list:
        print(word.upper())


print("Testing print_upper_words, expecting WHY HELLO THERE over 3 lines")
print_upper_words(["WHY", "hElLo", "tHEre"])
