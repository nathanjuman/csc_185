from A2 import ShoppingCart

# purpose: Obtain an action from user and perform it
# input: cart - the current shopping cart.
# output: none


def action(cart):
    valid_actions = ['a', 'r', 'd', 'q']
    prompt = "\nPick an action: \n a - to add an item \n r - to remove item(s) \n d - to display the cart \n q - to quit and purchase \n"
    action = getValidAction(valid_actions, prompt)

    while action != 'q':
        if action == 'a':
            add(cart)
        elif action == 'r':
            remove(cart)
        else:
            display(cart)
        action = getValidAction(valid_actions, prompt)

# purpose: Obtain an valid action from user
# inputs: actions - valid actions user can perform,
#        prompt - what to display to user
# outputs: a valid action


def getValidAction(actions, prompt):
    act = ""
    act = input(prompt)
    while act not in actions:
        act = input(prompt)
    return act

# purpose: Obtain a number from the user.
# inputs: prompt - instructions given to the user.
# output: Returns the number entered by user.


def getNumber(prompt):
    response = input(prompt)
    ans = None
    while ans == None:
        try:
            ans = float(response)
        except ValueError:
            print("Please enter a numeric value")
            response = input(prompt)
    return ans

# purpose: Obtain item name, price and quantity and add item to cart
# inputs: cart - the current shopping cart.
# outputs: the item is added to cart


def add(cart):
    name = input("Enter name of item to add: ")
    price = getNumber("Enter the item price: ")
    q = getNumber("Enter the item quantity: ")
    cart.add(name, price, q)

# purpose: Obtain item name and quantity to delete from cart
# inputs: cart - the current shopping cart.
# outputs: the given quantity of the item is deleted from cart


def remove(cart):
    name = input("Enter name of item to remove: ")
    a = getNumber("Enter the item quantity to remove: ")
    cart.remove(name, a)

# purpose: Display list of items in the cart and the most expensive item
# inputs: cart - the current shopping cart.
# outputs: Display cart, total, and most expensive item


def display(cart):
    if cart.size() > 0:
        print("The cart of cost $", cart.totalPrice(), " contains:\n", cart)
        print("The most expensive item in the cart is:", cart.mostExpensive())
    else:
        print("Your cart is empty")

# purpose: Display list of items in the cart and the total payment
# inputs: cart - the current shopping cart.
# outputs: Display cart and the total payment


def quit(cart):
    if cart.size() > 0:
        print("You are purchasing:\n", cart)
        print("Your total payment is: $", cart.totalPrice())
    else:
        print("Your cart is empty. No payment necessary")


def main():
    cart = ShoppingCart()
    action(cart)
    quit(cart)
main()
