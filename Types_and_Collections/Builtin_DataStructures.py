# Array / Stack / Queue
array = []  # note: lists are implemented as dynamically-sized arrays
array.append(1); array.pop()    # Stack - fast, O(1) push+pop
array.append(1); array.pop(0)   # Queue - slow, O(1) enqueue, O(n) dequeue
from collections import deque   # Queue - fast, O(1) enqueue+dequeue
queue = deque(); queue.append(1); queue.popleft()


# Hash Table
hashtable = {}


# Linked List / Graph
class Node:
    value = None
    pointers = []


# Binary Search Tree
# basically never used in Python - only reason for BSTs is in-order traversal,
# which the sortedcontainers package does faster anyways


# Priority Queue (stored in a list)
import heapq

# Min Heap:
heap = [6, 3, 5, 2, 4, 1]
heapq.heapify(heap)   # heap is now [[1, 3, 5, 2, 4, 6]]
def heapSort(iterable): 
    heap = []
    for item in iterable:
        heapq.heappush(heap, item)
    return [heapq.heappop(heap) for i in range(len(heap))]

# Max Heap:
heap = [6, 3, 5, 2, 4, 1]
heapq._heapify_max(heap)   # heap is now [[1, 3, 5, 2, 4, 6]]
def heapSort(iterable): 
    heap = []
    for item in iterable:
        heapq._heappush_max(heap, item)
    return [heapq._heappop_max(heap) for i in range(len(heap))]