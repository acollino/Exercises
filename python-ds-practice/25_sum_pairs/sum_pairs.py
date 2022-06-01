def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    best_pair = [(), len(nums)]
    for index_start in range(len(nums)):
        num_A = nums[index_start]
        for index_end in range(index_start + 1, len(nums)):
            num_B = nums[index_end]
            if num_A + num_B == goal:
                if index_end < best_pair[1]:
                    best_pair = [(num_A, num_B), index_end]
    return best_pair[0]
