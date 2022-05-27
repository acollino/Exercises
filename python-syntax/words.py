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


def print_e_words(word_list):
    """
    Given a list of strings, print each string that starts with 'e', 
    regardless of case, in uppercase on a separate line.
    """
    for word in word_list:
        if word.startswith(("E", "e")):
            print(word.upper())


print("Testing print_e_words, expecting 'EVIL EGGPLANT ELUDES EEL' over 4 lines")
print_e_words(["Evil", "eggplant", "Parmesan", "ELUDES", "friendly", "eel"])


def print_matching_words(word_list, must_start_with):
    """
    Given a list of strings and a set of letters, print each string that starts 
    with a letter in the set, regardless of case, in uppercase on a separate line.
    """
    for letter in must_start_with:
        for word in word_list:
            if word.startswith((letter.lower(), letter.upper())):
                print(word.upper())


print("Testing print_matching_words, expecting 'PARMESAN FRIENDLY' over 2 lines")
print("Sets are unordered, so the order of printing cannot be guaranteed")
print_matching_words(["Evil", "eggplant", "Parmesan",
                     "ELUDES", "friendly", "eel"], {"p", "f", "a"})
