from dieclass import MSDie


class SetOfDie:
    # Purpose: Create a SetOfDie containing the given number of dice where each die has the given number of sides
    # Input: sides and number of dice, both ints
    # Output: none
    def __init__(self, sides, number):
        self.dice = []
        self.sides = sides  # save sides to use in add method
        for i in range(number):
            d = MSDie(sides)  # make a MSDie object
            self.dice.append(d)  # put object into list

    # Purpose:Return a string representation of this object
    # Input: none
    # Output: returns a string where each die is on a new line
    def __str__(self):
        dicestr = ""
        for i in self.dice:
            dicestr = dicestr + "\n" + str(i)  # calling magic method __str__
        return dicestr

    # Purpose: Add a die to this collection
    # Input: none
    # Output: none
    def add(self):
        self.dice.append(MSDie(self.sides))

    # Purpose: rolls each die in the collection and returns the sum of all the rolled values of the dice
    # Input: none
    # Output: number,
    # Assumptions:
    def rollsum(self):
        ans = 0
        for die in self.dice:
            r = die.roll()
            ans = ans + r
        return ans

    # Purpose: rolls all the dice and returns the max and min rolled values over all die
    # Input: none
    # Output: two numbers
    # Assumptions:
    def rollmaxmin(self):
        rolls = []
        for die in self.dice:
            r = die.roll()
            rolls.append(r)
        max_value = max(rolls)
        min_value = min(rolls)
        return min_value, max_value

    # Purpose: returns true if this set’s dice have more sides than the other set’s dice
    # Input: other
    # Output: boolean
    def __gt__(self, other):
        return self.sides > other.sides

    # Purpose: increments the value of every dice in list whose value is less than sides / 2
    # Input: none
    # Output: none
    def update(self):
        for die in self.dice:
            r = die.roll()
            if r < (self.sides // 2):
                r += 1


def main():
    d = SetOfDie(10, 5)
    print(d)  # Expect: a list of 5 dice each with a random value between 1 and 10
    d.add()
    d.add()
    print(d)  # Expect: a list of 7 dice each with a random value between 1 and 10
    dsum = d.rollsum()
    print(dsum)  # Expect: the sum of all values between 1 and 10 rolled on 7 dice
    d_max_min = d.rollmaxmin()
    print(d_max_min)  # Expect: the max and min values rolled in the set of die
    d2 = SetOfDie(8, 5)
    d3 = SetOfDie(12, 5)
    print(d > d2)  # Expect: True
    print(d > d3)  # Expect: False
    print(d2 < d3)  # Expect: True
    print(d == d3)  # Expect: False
    d4 = SetOfDie(11, 3)
    d4.update()
    print(d4)  # Expect: Each die value that was less than the number of sides divided by 2 was incremented by 1


main()
