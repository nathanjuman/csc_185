from stackDS import Stack
from queueDS import Queue

#purpose: Read the weights from a given filename and return as a list of ints
#assumptions:  file formatted with all weights on one line separated by spaces
#inputs: filename is the name of the file with the weights data
#output: Returns a list of ints containing the weights
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


#purpose: Obtain a number from the user.
#inputs: prompt - instructions given to the user.
#output: Returns number entered by user.
def getNumber(prompt):
    response = input(prompt)
    ans=None
    while ans == None:
        try:
            ans = float(response)
        except ValueError:
            print("Please enter a numeric value!")
            response = input(prompt)
    return ans

#purpose: finds the loading order for the aircraft given weights of bags 
#inputs: weightlist - an int list containing bag weights
#        maxweight - the max weight of a container
#output: Returns a stack containing containers in the aircraft loading order
def compute_order(weightlist, maxweight):
    '''TODO: complete this function '''

#purpose: builds a string containing the loading order for the aircraft 
#inputs: order - a stack with containers in the the aircraft loading order
#output: Returns a string containing the aircraft loading order
def str_order(order):
    order_str = ""
   '''TODO: complete this function'''
    return order_str
    
def main():
    filename = input("Enter filename: ") #get filename
    list_of_weights = get_weight_list(filename) #read weights from file into list
    
    if list_of_weights == None:
        return
    
    max_weight = getNumber("Enter container weight: ") #get container weight
    print("The aircraft unloading order is:") 
    order = compute_order(list_of_weights, max_weight) #get the aircraft loading order
    print(str_order(order)) #print loading order
