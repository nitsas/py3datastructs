#!/usr/bin/env python3


import unittest
import random
# modules I've written:
import binary_heap


class BinaryHeapTestCase(unittest.TestCase):
    """
    Test binary_heap.
    """
    def setUp(self):
        self.empty_heap = binary_heap.BinaryHeap()
    
    def test_empty_heap(self):
        """
        Test the empty heap.
        """
        self.assertEqual(len(self.empty_heap), 0)
        self.assertRaises(LookupError, self.empty_heap.peek)
        self.assertRaises(LookupError, self.empty_heap.pop)
    
    def test_random_insertions_and_pops(self):
        """
        Test the heap on a string of random insertions and pops.
        """
        def extract_min_element_of_list(list_):
            min_item = list_[0]
            min_index = 0
            for index, item in enumerate(list_):
                if item < min_item:
                    min_item = item
                    min_index = index
            list_.pop(min_index)
            return min_item
        # make a series of random items
        items = []
        for i in range(2000):
            priority = random.randint(-1000, 1000)
            items.append((priority, str(priority)))
        # make a heap
        heap = binary_heap.BinaryHeap()
        # insert the items all the while doing some random pops
        # this will keep track of the items that should be inside the heap
        items_in_heap = []
        for item in items:
            # insert item in the heap
            heap.insert(item)
            # keep track of the items that are in the heap
            items_in_heap.append(item)
            # one time out of ten pop the top (i.e. smallest) item
            if random.randint(1, 10) == 1:
                # pop top item 
                peeked_item = heap.peek()
                popped_item = heap.pop()
                # make sure that peek and pop referred to the same item
                self.assertEqual(peeked_item, popped_item)
                # make sure that popped item is the min of the items 
                # inserted so far
                true_min = extract_min_element_of_list(items_in_heap)
                self.assertEqual(popped_item, true_min)
            # make sure that len(heap) works correctly
            self.assertEqual(len(heap), len(items_in_heap))
        # make sure that remaining items will be popped in the correct order
        items_in_heap.sort(reverse=True)
        while len(items_in_heap) > 0:
            # make sure that peed and pop refer to the same item
            peeked_item = heap.peek()
            popped_item = heap.pop()
            self.assertEqual(peeked_item, popped_item)
            # make sure that pop always returns a min item
            true_min = items_in_heap.pop()
            self.assertEqual(popped_item, true_min)
            # make sure that len(heap) works:
            self.assertEqual(len(heap), len(items_in_heap))
        # the heap should be empty now:
        self.assertEqual(len(heap), 0)
        self.assertRaises(LookupError, heap.peek)
        self.assertRaises(LookupError, heap.pop)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
