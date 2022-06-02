def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # First attempt:
    # working_string = phrase.lower().replace(" ", "")
    # counter = len(working_string) - 1
    # for letter in working_string:
    #     if letter != working_string[counter]:
    #         return False
    #     if counter <= (len(working_string) - 1)/2:
    #         return True
    #     counter -= 1
    # return None

    simplified_string = phrase.lower().replace(" ", "")
    return simplified_string == simplified_string[::-1]
