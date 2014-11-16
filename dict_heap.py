"""
A pseudo-heap implemented using a dictionary.

Operations:  
- __len__
- insert
- pop / pop_min
- peek / find_min
- decrease_key

I use this until I find the time to implement a Fibonacci heap.

Author:  
  Christos Nitsas  
  (nitsas)  
  (chrisnitsas)

Language:
  Python 3(.4)

Date:
  August, 2014
"""


__all__ = ['DictHeap']


class DictHeap:
    """
    A pseudo-heap implemented using a dictionary.
    
    I use this until I find the time to implement a Fibonacci heap.
    """
    def __init__(self):
        """Initialize an empty heap."""
        self._items = {}
    
    def __len__(self):
        """Return the number of items in the heap as an int."""
        return len(self._items)
    
    def insert(self, item, item_key):
        """
        Insert a new item with key item_key to the heap.
        
        item -- the item to be inserted
        item_key -- the item's key
        
        If the item was already in the heap just update its key.
        """
        self._items[item] = item_key
    
    def decrease_key(self, item, new_item_key):
        """
        Update the item's key in the heap.
        
        This can even increase the item key.
        """
        self._items[item] = new_item_key
    
    def peek(self):
        """
        Return the item with the lowest key currently in the heap; None if 
        the heap is empty.
        
        Careful if the heap actually contains items set to None; in that case,
        this method returning None doesn't necessarily mean the heap is empty.
        """
        min_item = None
        min_key = float('inf')
        for item, key in self._items.items():
            if key < min_key:
                min_item = item
                min_key = key
        return min_item
