"""
A simple Union-Find data structure implementation.

author: 
Christos Nitsas
(chrisn654 or nitsas)

language:
Python 3(.4)

date:
July, 2014
"""


class UnionFindSimpleImpl:
    """
    A simple Union-Find data structure implementation.
    
    If n is the number of items in the structure, a series of m union 
    operations will take O(m * log(n)) time. Find operations are (amortized)
    constant time (O(1)) though.
    """
    def __init__(self, items):
        """Initialize the Union-Find structure from an iterable."""
        self._items = set(items)
        self._leader = dict()
        self._followers = dict()
        self._cluster_size = dict()
        for item in self._items:
            self._leader[item] = item
            self._followers[item] = [item]
            self._cluster_size[item] = 1
    
    def __getitem__(self, item):
        """
        Returns the cluster (i.e. the cluster's leader) that the 
        given item belongs to.
        
        Equivalent to UnionFindStructure.find().
        """
        return self._leader[item]
    
    
    def find(self, item):
        """
        Returns the cluster (i.e. the cluster's leader) that the 
        given item belongs to.
        
        Equivalent to UnionFindStructure.__getitem__().
        """
        return self[item]
    
    def union(self, leader_A, leader_B):
        """
        Joins together the two clusters that items leader_A 
        and leader_B represent.
        """
        if leader_A == leader_B:
            return
        if self._cluster_size[leader_B] > self._cluster_size[leader_A]:
            leader_A, leader_B = leader_B, leader_A
        for follower in self._followers[leader_B]:
            self._leader[follower] = leader_A
        self._followers[leader_A].extend(self._followers[leader_B])
        del(self._followers[leader_B])
        self._cluster_size[leader_A] += self._cluster_size[leader_B]
        del(self._cluster_size[leader_B])
    
    def joined(self, item_a, item_b):
        """
        Return True it the items belong to the same cluster; False otherwise.
        """
        if self.find(item_a) == self.find(item_b):
            return True
        else:
            return False
    
    def num_clusters(self):
        """Returns the current number of clusters."""
        return len(self._cluster_size)
    
    def items(self):
        """Returns a set containing all the items in the structure."""
        return self._items


class UnionFindUnionByRankAndPathCompression:
    """
    A faster Union-Find implementation with lazy unions (using union by 
    rank) and path compression.
    
    A series of m union & find operations on a structure with n items 
    will need time O(m * a(n)), where a(n) is the reverse Ackerman 
    function.
    """
    def __init__(self, items):
        """Initialize the Union-Find structure from an iterable."""
        raise(NotImplementedError)
    
    def __getitem__(self, item):
        """
        Returns the cluster (i.e. the cluster's leader) that the 
        given item belongs to.
        
        Equivalent to UnionFindStructure.find().
        """
        raise(NotImplementedError)
    
    
    def find(self, item):
        """
        Returns the cluster (i.e. the cluster's leader) that the 
        given item belongs to.
        
        Equivalent to UnionFindStructure.__getitem__().
        """
        raise(NotImplementedError)
    
    def union(self, leader_A, leader_B):
        """
        Joins together the two clusters that items leader_A 
        and leader_B represent.
        """
        raise(NotImplementedError)
    
    def num_clusters(self):
        """Returns the current number of clusters."""
        raise(NotImplementedError)
    
    def items(self):
        """Returns a set containing all the items in the structure."""
        raise(NotImplementedError)


_default_impl = UnionFindSimpleImpl


class UnionFindStructure:
    """
    A Union-Find data structure interface.
    
    It relies on a concrete Union-Find implementation such as 
    UnionFindSimpleImpl or UnionFindLazyUnionsAndPathCompressionImpl.
    """
    def __init__(self, items, *, impl=_default_impl):
        self._impl = impl(items)
    
    def __getitem__(self, item):
        return self._impl.__getitem__(item)
    
    def __getattr__(self, name):
        return getattr(self._impl, name)


