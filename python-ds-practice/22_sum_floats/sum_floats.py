def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    # original attempt
    # sum = 0
    # for number in nums:
    #     if isinstance(number, float):
    #         sum += number
    # return sum

    return sum(filter(lambda x: isinstance(x, float), nums))

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
