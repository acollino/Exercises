def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    num_open_parenths = 0
    for char in parens:
        if char == "(":
            num_open_parenths += 1
        elif char == ")":
            if num_open_parenths == 0:
                return False
            else:
                num_open_parenths -= 1
    return num_open_parenths == 0
