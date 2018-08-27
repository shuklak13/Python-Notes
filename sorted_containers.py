# https://github.com/grantjenks/python-sortedcontainers/

from sortedcontainers import *

# SortedList - an order statistic tree
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
    # creates SortedList(['a', 'b', 'c', 'd', 'e'])
slwk = SortedList([1, 2, 3, 4, 5], key = lambda x: -x)
    # creates SortedListWithKey([5, 4, 3, 2, 1], key = lambda x: -x)
# Runtime
    # __init__(list) - O(nlogn)
    # add(x) - O(logn)
    # remove(x) - O(logn)
    # index(x) - O(logn)
    # bisect_left(x) - O(logn) - returns # of elems y where y < x
    # bisect_right(x) - O(logn) - returns # of elems y where y <= x
    # irange(x, y) - O(n) - returns iterator over elems between values x and y
    # islice(i, j) - O(n) - returns iterator over elems between indices i and j

# SortedDict = Dictionary + SortedList
sd = SortedDict({'d': 4, 'b': 2, 'c': 3})                   # init
sdwk = SortedDict(lambda x: -x, {'d': 4, 'b': 2, 'c': 3})   # init w/ key  
sd['e'] = 5             # update; returns {'b':2, 'c':3, 'd':4, 'e'=5}
sd['b']                 # query 'b' by key
sd.peekitem(index=-1)   # query 'e' by order
sd.pop('b')             # pop 'b' by key
sd.popitem(index=-1)    # pop 'e' by order
sd.index('c')           # same as SortedList
sd.bisect_left('c')     #   |   |   |   |
sd.bisect_right('c')    # same as SortedList

# SortedSet = Dictionary + SortedList
ss = SortedSet('ba')                    # init
sdwk = SortedSet('ba', lambda x: -x)    # init w/ key
ss.add('c')     # add
'c' in ss       # search
ss.index('c')   # index
ss.remove('c')  # remove
# SortedDict/Set runtimes are worst-case between Dict/Set and SortedList
    # O(nlogn) for init
    # O(1) for search
    # O(logn) for add, remove, index

# make your own DefaultSortedDict   (like defaultdict)
class DefaultSortedDict(SortedDict):
    def __missing__(self, key):
        return 0
dsd = DefaultSortedDict()
dsd['z']    # returns 0