class Item:
    ''' Represents items that can be stored in a shopping cart: 
        Attributes: name, stores the name of the item
                    price, stores the price for a single quantity of the item
                    quantity, stores the quantity of this item purchased
    '''

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # purpose: increases the objects quantity by the given amount
    # input: amt, number given by user
    # output: none
    def updateQuantity(self, amt):
        self.quantity = self.quantity + amt

    # purpose: returns the total price of an order
    # input: none
    # output: number
    def getTotal(self):
        return self.price * self.quantity

    # purpose: returns a string with the item information
    # input: none
    # output: text with item information
    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}, Price per Item: {self.price}"

    # purpose: returns true if the item has the same name as the other item, otherwise false
    # input: other, item given by user
    # output: boolean
    def __eq__(self, other):
        return self.name == other.name

    # purpose: returns true if an item has a price greater than the other item given, otherwise false
    # input: other, item given by user
    # output: boolean
    def __gt__(self, other):
        return self.price > other.price


class ShoppingCart:
    ''' Represents a shopping cart that stores a list of item objects 
        Attributes: itemList, a list storing item objects
    '''

    def __init__(self):
        self.itemList = []

    # purpose: adds item object to itemList, if item already exists the quantity is adjusted
    # input: name of item, price of single quantity, quantity of item
    # output: None
    def add(self, name, price, quantity):
        for item in self.itemList:
            if name == item.name:
                item.quantity += quantity
                return
        self.itemList.append(Item(name, price, quantity))

    # purpose: reduces item object quantity by the given amount, if the quantity goes to 0 or is less than 0 the item is removed from itemList
    # input: name of item, amount to decrease the quantity
    # output: None
    def remove(self, name, amt):
        for item in self.itemList:
            if name == item.name:
                if amt >= item.quantity:
                    self.itemList.remove(item)
                else:
                    item.quantity -= amt

    # purpose: returns the item object which has the highest item price
    # input: none
    # output: string item, or None if itemList is empty
    def mostExpensive(self):
        if len(self.itemList) == 0:
            return None
        else:
            max_price = 0
            max_item = ""
            for item in self.itemList:
                if item.price > max_price:
                    max_price = item.price
                    max_item = item.name
            return max_item

    # purpose: returns the total price of all items in itemList
    # input: none
    # output: number, returns 0 if itemList is empty
    def totalPrice(self):
        sum = 0
        if len(self.itemList) == 0:
            return 0
        else:
            for item in self.itemList:
                sum = sum + item.getTotal()
            return sum

    # purpose: returns a string containing the string version of each item on a new line
    # input: none
    # output: string (each item on seperate line)
    def __str__(self):
        cart_str = ""
        for item in self.itemList:
            cart_str = cart_str + '\n' + str(item)
        return cart_str

    # purpose: returns the number of items in the cart with unique names
    # input: none
    # output: number
    def size(self):
        uniqueItems = []
        for item in self.itemList:
            if item.name not in uniqueItems:
                uniqueItems.append(item.name)
        return len(uniqueItems)


def main():
    # Item:
    thing_1 = Item('apple', 3, 5)
    thing_2 = Item('banana', 2, 3)
    thing_3 = Item('apple', 3, 2)
    thing_4 = Item('kiwi', 6, 3)

    print(thing_1)  # expect: Item: apple, Quantity: 5, Price per Item: 3

    thing_1.updateQuantity(2)
    thing_2.updateQuantity(3)
    print(thing_1)  # expect: Item: apple, Quantity: 7, Price per Item: 3
    print(thing_2)  # expect: Item: banana, Quantity: 6, Price per Item: 2

    print(thing_1.getTotal())  # expect: 21
    print(thing_4.getTotal())  # expect: 18

    print(thing_1 == thing_2)  # expect: False
    print(thing_1 == thing_3)  # expect: True

    print(thing_1 > thing_2)  # expect: True
    print(thing_1 > thing_4)  # expect: False

    # Shopping Cart:
    cart1 = ShoppingCart()
    cart1.add('apple', 2, 5)
    cart1.add('banana', 6, 3)
    cart1.add('kiwi', 5, 4)
    print(cart1)
    # expect: each string version of the item objects in itemList on a new line
    cart1.add('apple', 2, 3)
    print(cart1)  # expect: the quantity of apples to increase from 5 to 8

    cart1.remove('apple', 3)
    print(cart1)  # expect: quantity of apples to decrease from 8 to 5
    cart1.remove('kiwi', 4)
    cart1.remove('banana', 10)
    print(cart1)  # expect: the kiwi and bananas are removed from the cart

    cart2 = ShoppingCart()
    print(cart2.mostExpensive())  # expect: None
    cart2.add('cookies', 7, 10)
    cart2.add('cake', 15, 1)
    cart2.add('donut', 3, 12)
    print(cart2.mostExpensive())  # expect: cake

    cart3 = ShoppingCart()
    print(cart3.totalPrice())  # expect: 0
    print(cart1.totalPrice())  # expect: 10
    print(cart2.totalPrice())  # expect: 121

    print(cart1.size())  # expect: 1
    print(cart2.size())  # expect: 3
    print(cart3.size())  # expect: 0


main()

'''
Question 4: Short Answer

When users choose to add an item price or item quantity, or remove a quantity, the function getNumber() is called. In that function is an ValueError exception that prevents users from entering a string for an integer input. If a user enters a string, instead of the program execution stopping compeletely - the exception allows the program to alter the flow of control to continue the prompt until it receives an integer from the user. 

'''
