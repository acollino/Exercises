def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # original attempt:
    # for index_first in range(len(nums)):
    #     num_A = nums[index_first]
    #     for index_second in range(index_first + 1, len(nums)):
    #         if nums[index_second] == num_A:
    #             return num_A
    # return None

    for index in range(len(nums)):
        if nums[index] in nums[index + 1:]:
            return nums[index]
    return None

    # The loop could also be replaced by a filter(), such as:
    # list(filter(lambda x: nums[x] in nums[x+1:], range(len(nums))))
    # or  [index for index in range(len(nums)) if nums[index] in nums[index+1:]]
    # but it would also require verifying if the list is not empty before
    # returning the first (and only) value or None
