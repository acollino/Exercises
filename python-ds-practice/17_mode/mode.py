def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Original attempt:
    # value_counter = {}
    # most_times = 0
    # mode = -1
    # for number in nums:
    #     num_times = value_counter.get(number, -1)
    #     if num_times == -1:
    #         value_counter.update({number: 1})
    #     else:
    #         value_counter.update({number: num_times + 1})
    #     if value_counter.get(number) > most_times:
    #         most_times = value_counter.get(number)
    #         mode = number
    # return mode

    value_counter = {num: nums.count(num) for num in nums}
    return max(value_counter, key=value_counter.get)
