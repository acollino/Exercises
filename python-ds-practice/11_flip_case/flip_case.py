def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap_phrase = ""
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            swap_phrase += letter.swapcase()
        else:
            swap_phrase += letter
    return swap_phrase
