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
        self.start = start 
        self.next = start
    
    def generate(self):
        """
            returns next value and increments the state of the value in the object

        """
        value = self.next
        self.next += 1 
        return value 
    
    def reset(self):
        """
            Resets next value to the start value
        """
        self.next = self.start 


    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={self.next}>'