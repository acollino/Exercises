def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # original attempt
    # for element in lst:
    #     if not isinstance(element, list):
    #         return False
    # return True

    return all(isinstance(el, list) for el in lst)
