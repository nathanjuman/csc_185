# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#queue.py

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []
    
    def is_empty(self):
        """Return True if the queue is empty, False Otherwise"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add the given item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove and return the item from the queue following FIFO"""
        return self._items.pop()

    def size(self):
        """Returns the number of items in the queue"""
        return len(self._items)
