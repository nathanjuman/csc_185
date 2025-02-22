from stackDS import Stack
from queueDS import Queue

# purpose: Read the weights from a given filename and return as a list of ints
# assumptions:  file formatted with all weights on one line separated by spaces
# inputs: filename is the name of the file with the weights data
# output: Returns a list of ints containing the weights


def get_weight_list(filename):
    file = None
    try:
        file = open(filename, 'r')
    except:
        print("Unable to open file", filename)
        return None
    line = file.readline()
    weightslist = [int(x) for x in line.split()]
    return weightslist


# purpose: Obtain a number from the user.
# inputs: prompt - instructions given to the user.
# output: Returns number entered by user.
def getNumber(prompt):
    response = input(prompt)
    ans = None
    while ans == None:
        try:
            ans = float(response)
        except ValueError:
            print("Please enter a numeric value!")
            response = input(prompt)
    return ans

# purpose: finds the loading order for the aircraft given weights of bags
# inputs: weightlist - an int list containing bag weights
#        maxweight - the max weight of a container
# output: Returns a stack containing containers in the aircraft loading order


def compute_order(weightlist, maxweight):
    container = Stack()
    bag_order = []
    weight = 0

    for i in range(len(weightlist)):
        if (weightlist[i] + weight > maxweight) or (weight == maxweight):
            container.push(bag_order)
            weight = 0
            bag_order = []
            bag_order.append(str(weightlist[i]))
            weight += weightlist[i]
        else:
            bag_order.append(str(weightlist[i]))
            weight += weightlist[i]

    if len(bag_order) > 0:
        container.push(bag_order)

    return container

# purpose: builds a string containing the loading order for the aircraft
# inputs: order - a stack with containers in the aircraft loading order
# output: Returns a string containing the aircraft loading order


def str_order(order):
    order_str = ""
    order_list = []

    while order.size() > 0:
        order_list += order.pop()

    order_str += ' '.join(order_list)
    return order_str


def main():
    filename = input("Enter filename: ")  # get filename
    # read weights from file into list
    list_of_weights = get_weight_list(filename)

    if list_of_weights == None:
        return

    max_weight = getNumber("Enter container weight: ")  # get container weight
    print("The aircraft unloading order is:")
    # get the aircraft loading order
    order = compute_order(list_of_weights, max_weight)
    print(str_order(order))  # print loading order


main()
