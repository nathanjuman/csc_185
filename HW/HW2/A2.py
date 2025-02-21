class Item:
    """ Represents items that can be stored in a shopping cart: """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def updateQuantity(self, amt):
        #Purpose: increases the objects quantity by the given amount
        #Input: amt, number given by user
        #Output: number

        self.quantity = self.quantity + amt

    def getTotal(self):
        #Purpose: returns the total price of an order
        #Input: none
        #Output: number

        return self.price * self.quantity

    def __str__(self):
        #Purpose: returns a string with the item information
        #Input: none
        #Output: text with item information

        return f"Item: {self.name}, Quantity: {self.quantity}, Price per Item: {self.price}"

    def __eq__(self, other):
        #Purpose: returns true if the item has the same name as the other item, otherwise false
        #Input: other, item given by user
        #Output: boolean

        return self.name == other.name

    def __gt__(self, other):
        #Purpose: returns true if an item has a price greater than the other item given, otherwise false
        #Input: other, item given by user
        #Output: boolean

        return self.price > other.price

def main():
    thing_1 = Item('apple', 3, 5)
    thing_2 = Item('banana', 2, 3)
    thing_3 = Item('apple', 3, 2)
    thing_4 = Item('kiwi', 6, 3)

    print(thing_1) #expect: Item: apple, Quantity: 5, Price per Item: 3

    thing_1.updateQuantity(2)
    thing_2.updateQuantity(3)
    print(thing_1) #expect: Item: apple, Quantity: 7, Price per Item: 3
    print(thing_2) #expect: Item: banana, Quantity: 6, Price per Item: 2

    print(thing_1.getTotal()) #expect: 21
    print(thing_4.getTotal()) #expect: 18

    print(thing_1 == thing_2) #expect: False 
    print(thing_1 == thing_3) #expect: True

    print(thing_1 > thing_2) #expect: True
    print(thing_1 > thing_4) #expect: False

main()