# Implementation of Queue using Circular List 
class Queue: 
    def __init__(self, n): # Constructor 
        self.capacity = n
        self.queue = [0] * n
        self.size = 0
        self.head = 0 # Front value
    
    def enqueue(self, x):
        if (not(self.capacity == self.size)):
            tail = (self.head + self.size) % self.capacity
            self.queue[tail] = x
            self.size = self.size + 1
        else:
            print("Queue OverFlow")
            return -1
        
    def dequeue(self):
        if (not(self.size == 0)):
            x = self.queue[self.head]
            self.head = (self.head + 1) % self.capacity
            self.size = self.size - 1
            return x
        else:
            print("Queue is UnderFlow")


if __name__ == "__main__":
    qu = Queue(4) # Object of class Queue 
    qu.enqueue(10)
    qu.enqueue(21)
    qu.enqueue(23)
    qu.enqueue(12)
    # qu.enqueue(11) # Queue OverFlow 
    qu.dequeue()
    qu.dequeue()
    qu.dequeue()
    qu.dequeue()
    qu.dequeue() # Queue UnderFlow