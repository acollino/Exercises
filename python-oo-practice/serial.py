"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create an instance of a SerialGenerator using a start value"""
        self.start = start
        self.increment = start - 1
    
    def generate(self):
        """
        Generate a value, increasing from start or the last value returned
        """
        self.increment += 1
        return self.increment

    def reset(self):
        """Reset the SerialGenerator to its starting value"""
        self.increment = self.start - 1