def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    list_to_return = []
    add_toggle = True
    for element in lst:
        if add_toggle:
            list_to_return.append(element)
        add_toggle = not add_toggle
    return list_to_return