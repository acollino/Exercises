def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    list_phrase = list(phrase)
    for index in range(len(list_phrase)):
        if list_phrase[index].lower() == to_swap.lower():
            list_phrase[index] = list_phrase[index].swapcase()
    return "".join(list_phrase)
