def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    # original attempt
    # followed_greater = 0
    # for index1 in range(len(nums)):
    #     for index2 in range(index1 + 1, len(nums)):
    #         if nums[index1] < nums[index2]:
    #             followed_greater += 1
    # return followed_greater

    greater_num_occurences = [val
                              for index in range(len(nums))
                              for val in nums[index+1:] if val > nums[index]]
    return len(greater_num_occurences)
