def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    string1 = str(num1)
    string2 = str(num2)
    for digit in string1:
        if string1.count(digit) != string2.count(digit):
            return False
    return True