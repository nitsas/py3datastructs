"""
A pseudo-heap implemented using a dictionary.

Operations:
- __len__
- insert
- pop / pop_min
- peek / find_min
- decrease_key

I use this until I find the time to implement a Fibonacci heap.

author:
Christos Nitsas
(chrisn654)
(nitsas)

language:
Python 3.4

date:
August, 2014
"""


__all__ = ["DictHeap"]


class DictHeap:
    """
    A pseudo-heap implemented using a dictionary.
    
    I use this until I find the time to implement a Fibonacci heap.
    """
    def __init__(self):
        """Initializes an empty heap."""
        self.items = {}
    
    def __len__(self):
        """Returns the number of items in the heap."""
        return len(self.items)
    
    def insert(self, item, item_key):
        """
        Insert a new item with key item_key to the heap.
        
        If the item was already in the heap just update its key.
        """
        self.items[item] = item_key
    
    def decrease_key(self, item, new_item_key):
        """Update the item's key in the heap."""
        self.items[item] = new_item_key
    
    def pop(self):
        """
        Remove and return the item with the lowest key currently in 
        the heap; None if the heap is empty.
        """
        min_item = None
        min_key = float("inf")
        for item, key in self.items.items():
            if key < min_key:
                min_item = item
                min_key = key
        return min_item
