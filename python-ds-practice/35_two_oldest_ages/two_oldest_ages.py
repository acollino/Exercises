def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    # original attempt
    # oldest_ages = [0, 0]
    # for age in ages:
    #     if age > oldest_ages[1]:
    #         oldest_ages[0] = oldest_ages[1]
    #         oldest_ages[1] = age
    #     elif age < oldest_ages[1] and age > oldest_ages[0]:
    #         oldest_ages[0] = age
    # return tuple(oldest_ages)
    
    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    oldest = max(ages)
    second_old = max(filter(lambda x: x!=oldest, ages))
    return (second_old, oldest)
