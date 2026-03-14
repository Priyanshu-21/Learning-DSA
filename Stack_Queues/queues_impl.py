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
    
    # Method to get head of queue
    def head(self):
        return self.elements[0]

    # Method to get tail of queue
    def tail(self):
        return self.elements[-1]
    
    def __len__(self):
        return len(self.elements)
    
    # Need to create next and iter object to traverse through elements 
    def __iter__(self):
        for element in self.elements:
            yield element

fifo = Queue()
# Add elements to the queue 
fifo.enqueue("First")
fifo.enqueue("Second")
fifo.enqueue("Third")

for f in fifo: 
    print(f)

print(len(fifo))
fifo.dequeue()
print(fifo.head())
print(fifo.tail())
