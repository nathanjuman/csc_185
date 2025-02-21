# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 


class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the stack following LIFO order"""
        return self._items.pop()

    def peek(self):
        """Returns the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Returns the number of items in the stack"""
        return len(self._items)
