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


def _swap(list_, a, b):
    """
    Swap items in positions a and b of list_.
    
    list_ -- a list
    a -- an index in list_
    b -- an index in list_
    """
    list_[a], list_[b] = list_[b], list_[a]


def _shift_up(list_, index, less):
    """
    Move a heap node up in the heap, as long as needed.
    
    list_ -- the heap as a list
    index -- the index of the node in list_
    less -- the callable we'll use to compare items
    """
    parent = (index - 1) // 2
    while index > 0 and not less(list_[parent], list_[index]):
        # swap item with its parent
        _swap(list_, index, parent)
        # update position pointers
        index = parent
        parent = (index - 1) // 2


def _shift_down(list_, index, less):
    """
    Move a heap node down in the heap, as long as needed.
    
    list_ -- the heap as a list
    index -- the index of the node in list_
    less -- the callable we'll use to compare items
    """
    # initialize the positions of the node's children
    # left child
    left = 2 * index + 1
    # right child
    right = left + 1
    # does the node actually have (both) children?
    if left >= len(list_):
        # no children
        return
    elif right >= len(list_):
        # only left child
        if less(list_[left], list_[index]):
            _swap(list_, index, left)
        return
    # node has two children
    while less(list_[left], list_[index]) or less(list_[right], list_[index]):
        # the item is *less* than at least one of its children
        # swap it with the *smallest* of its children
        if less(list_[left], list_[right]):
            _swap(list_, index, left)
            index = left
        else:
            _swap(list_, index, right)
            index = right
        # update child position pointers
        left = 2 * index + 1
        right = left + 1
        # does the node actually have (both) children?
        if left >= len(list_):
            # no children
            return
        elif right >= len(list_):
            # only left child
            if less(list_[left], list_[index]):
                _swap(list_, index, left)
            return


class BinaryHeap:
    """
    A simple binary heap implementation (using a list).
    
    A typical pattern for items is a tuple in the form: 
    (priority_number, data).
    """
    
    def __init__(self, compare=operator.lt):
        """
        Initialize an empty heap.
        
        compare -- the callable we'll use to compare items; should accept two
                   parameters (items); default: operator.lt (i.e. min-heap)
        
        By default the lowest valued items are retrieved first (the lowest 
        valued item is the one returned by `sorted(list(items))[0]`). Users
        must provide a different `compare` parameter if they want different
        behavior (e.g. `compare=operator.gt` for a max-heap).
        
        A typical pattern for items is a tuple in the form: 
        (priority_number, data)
        """
        self._items = []
        self._less = compare
    
    def __len__(self):
        """Return the number of items in the heap as an int."""
        return len(self._items)
    
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
        _shift_up(self._items, len(self._items) - 1, self._less)
    
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
        _swap(self._items, 0, -1)
        min_item = self._items.pop()
        # now repair the heap property
        _shift_down(self._items, 0, self._less)
        # return
        return min_item
