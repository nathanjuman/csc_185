import random


class MSDie:
    """
    Multi-sided die
    Attributes:
        num_sides: the number of sides this die has
        current_value - the value of the faced up side of this die
    """
    # Purpose:Constructs new objects of type MSDie with the given number of sides
    # Input: number of sides the die should have
    # Output:none

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    # Purpose:Sets the value of this die to a random value between 1 and its number of sides
    # Input: none
    # Output: returns the randomly rolled value of this die
    def roll(self):
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    # Purpose:Returns the value of this die as a string
    # Input: none
    # Output: none
    def __str__(self):
        return str(self.current_value)

    # Purpose:Returns true if this die's value is equal to the value of another die, false otherwise
    # Input: a MSDie object
    # Output: True or False
    def __eq__(self, other):
        return self.current_value == other.current_value

    # Purpose:Returns true if this die's value is less than another die's value, false otherwise
    # Input: a MSDie object
    # Output: True or False
    def __lt__(self, other):
        return self.current_value < other.current_value

    # Purpose:Returns true if this die's value is less than or equal to another die's value, false otherwise
    # Input: a MSDie object
    # Output: True or False
    def __le__(self, other):
        return self.current_value <= other.current_value
