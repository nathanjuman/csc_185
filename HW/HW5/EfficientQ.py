class Queue:

    def __init__(self):
        self.queue_dict = {}
        self.head = 1
        self.tail = 1

    # purpose: adds an item to the rear of the queue
    # input: item
    # output: none
    # assumptions: none
    def enqueue(self, item):
        if self.tail == 1:
            self.queue_dict[item] = self.head
            self.tail += 1
        else:
            self.queue_dict[item] = self.tail
            self.tail += 1

    # purpose: removes the item from the front of the queue
    # input: none
    # output: none
    # assumptions: the queue is not empty
    def dequeue(self):
        del self.queue_dict[self.head]
        self.head += 1

    # purpose: returns True if the queue is empty, otherwise false
    # input: none
    # output: boolean
    # assumptions: none
    def is_empty(self):
        return len(self.queue_dict) == 0

    # purpose: returns the size of the queue
    # input: none
    # output: int
    # assumptions: none
    def size(self):
        return len(self.queue_dict)

    # purpose: returns the current status of the queue
    # input: none
    # output: dictionary
    # assumptions: none
    def currentQueue(self):
        return self.queue_dict


def main():
    groceryLine = Queue()
    groceryLine.enqueue(1)
    groceryLine.enqueue(2)
    groceryLine.enqueue(3)
    print(groceryLine.currentQueue())  # expect: {1: 1, 2: 2, 3: 3}

    groceryLine.dequeue()
    print(groceryLine.currentQueue())  # expect: {2: 2, 3: 3}

    print(groceryLine.size())  # expect: 2
    groceryLine.enqueue(4)
    print(groceryLine.currentQueue())

main()
