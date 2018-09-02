from collections import *

# Deque: O(1) insertion and removal on both ends
d = deque()
d.append(1); d.pop()        # Stack
d.append(1); d.popleft()    # Queue
d.rotate(2) # equivalent to d.appendLeft(d.pop()) twice

# Counter: a dictionary optimized for counting
    # functions: "most_common", "update" (add), and "subtract"
c = Counter('aaaaaaaaabbbbbbbcc');
c.most_common(3) # [('a', 9), ('b', 7), ('c', 2)]
d = Counter({'a': 1, 'b': 2, 'c': 3})
c.subtract(d);  c   # Counter({'a': 8, 'b': 5, 'c': -1})
c.update(d);    c   # Counter({'a': 9, 'b': 7, 'c': 2})

# Default Dict: automatically does dict.setdefault() for you
    # choose the default data type (list, int, set, dict, etc.) at creation time
d = defaultdict(list)
for k, v in [('yellow', 1), ('blue', 2), ('red', 1), ('blue', 4)]:
     d[k].append(v)
d = {}
for k, v in [('yellow', 1), ('blue', 2), ('red', 1), ('blue', 4)]:
    d.setdefault(k, []).append(v)

# Ordered Dict: remembers key insertion order   (doesn't care about value)
    # 'move_to_end' lets you shuffle items to front or back
d = OrderedDict.fromkeys('abcd')
print(d)                                    # odict_keys(['a', 'b', 'c', 'd'])
d.move_to_end('b'); print(d)                # odict_keys(['a', 'c', 'd', 'b'])
d.move_to_end('b', last=False); print(d)    # odict_keys(['b', 'a', 'c', 'd'])