# Implementation of queues using dequeue (Traversal, insert, delete and search)
from collections import deque

# Create a queue class to have traversal and inserting, deleting values 
class Queue():

    def __init__(self):
        # Define queue
        self.elements = deque()
    
    # Enqueue method 
    def enqueue(self, value):
        # In queue, enqueue happens in the last 
        self.elements.append(value)

    # Dequeue method 
    def dequeue(self):
        # In queue, dequeue happens for the first element 
        return self.elements.popleft()
    
    # Need to create next and iter object to traverse through elements 
    def __iter__(self):
        yield self.elements

fifo = Queue()
# Add elements to the queue 
fifo.enqueue("First")
fifo.enqueue("Second")
fifo.enqueue("Third")

# Let see which values are popped out first and last 
# Can we iterator through this values ? ans (iterator & Generator)
for f in fifo: 
    print(f)

