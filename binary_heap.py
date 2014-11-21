"""
A simple binary heap implementation (using a list).

Operations:  
- __len__
- insert 
- pop
- peek

TODO:
- Add operations: heapify (maybe in __init__)

Author:  
  Christos Nitsas  
  (nitsas)  
  (chrisnitsas)

Language:
  Python 3(.4)

Date:
  November, 2014
"""


import operator


__all__ = ['BinaryHeap']


class BinaryHeap:
    """
    A simple binary (min) heap implementation (using a list).
    
    The lowest valued items are retrieved first (the lowest valued item is
    the one returned by `sorted(list(items))[0]`). A typical pattern for
    items is a tuple in the form: (priority_number, data).
    """
    
    def __init__(self):
        """Initialize an empty (min) heap."""
        self._items = []
        self._less = operator.lt
    
    def __len__(self):
        """Return the number of items in the heap as an int."""
        return len(self._items)
    
    def _swap(self, a, b):
        """
        Swap items in positions `a` and `b` of `self._items`.
        """
        self._items[a], self._items[b] = self._items[b], self._items[a]
    
    def _shift_up(self, node):
        """
        Move node up in the tree, as long as needed.
        
        node -- the position of the node in self._items
        """
        parent = (node - 1) // 2
        while node > 0 and not self._less(self._items[parent],
                                          self._items[node]):
            # swap item with its parent
            self._swap(node, parent)
            # update position pointers
            node = parent
            parent = (node - 1) // 2
    
    def _shift_down(self, node):
        """
        Move node down in the tree, as long as needed.
        
        node -- the position of the node in self._items
        """
        # initialize the positions of the node's children
        # left child
        left = 2 * node + 1
        # right child
        right = left + 1
        while self._less(self._items[left], self._items[node]) or \
              self._less(self._items[right], self._items[node]):
            # the item is *less* than at least one of its children
            # swap it with the *smallest* of its children
            if self._less(self._items[left], self._items[right]):
                self._swap(node, left)
                node = left
            else:
                self._swap(node, right)
                node = right
            # update child position pointers
            left = 2 * node + 1
            right = left + 1
    
    def insert(self, item):
        """
        Insert a new item.
        
        item -- the item to be inserted
        
        A typical pattern for items is a tuple in the form: 
        (priority_number, data)
        
        This operation's time complexity is `O(log(n))`, where `n` is the
        number of items in the heap.
        """
        # insert item at the end of the list of items
        self._items.append(item)
        # shift the item up as needed to restore the heap property
        self._shift_up(len(self._items) - 1)
    
    def peek(self):
        """
        Return the item on top of the heap without removing the item.
        
        Return the item with the *lowest* value according to the heap's
        (partial) ordering (e.g. the min item if we have a min heap).
        
        Raises a `LookupError('peek into empty heap')` if the heap is empty.
        """
        if len(self._items) == 0:
            raise LookupError('peek into empty heap')
        return self._items[0]
    
    def pop(self):
        """
        Remove and return the item that's currently on top of the heap. 
        
        Remove and return the item with the *lowest* value according to the 
        heap's (partial) ordering (e.g. the min item if we have a min heap).
        
        Raises a `LookupError('pop from empty heap')` if the heap is empty.
        """
        if len(self._items) == 0:
            raise LookupError('pop from empty heap')
        # else:
        # swap top item with the last item of self._items, and remove it
        self._swap(0, -1)
        min_item = self._items.pop()
        # now repair the heap property
        self._shift_down(0)
        # return
        return min_item
