# Implementation of Queue using List 
class Queue: 
    def __init__(self, n): # Constructor 
        self.size = n
        self.queue = [0] * n # Create a list of all 0 elements
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (not(self.tail == self.size)):
            self.queue[self.tail] = x
            self.tail = self.tail + 1
        else: 
            print("Queue is OverFlow")
            return -1
        
    def dequeue(self):
        if (not(self.head == self.size)):
            x = self.queue[self.head]
            self.head = self.head + 1
            return x
        else: 
            print("Queue is UnderFlow")
            return -1


if __name__ == "__main__":
    qu = Queue(4) # qu is object for concept (class) Queue
    qu.enqueue(10)
    qu.enqueue(5)
    qu.enqueue(3)
    qu.enqueue(14)
    qu.dequeue()
    qu.dequeue()
    qu.dequeue()
    qu.dequeue()
    qu.dequeue() # Queue is underFlow 
    