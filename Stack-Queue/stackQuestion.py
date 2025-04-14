# Implement two stack in one array (deque) such that it will not overflow 
from collections import deque
import math 

class Stack:
    def __init__(self, n): #Constructor
        self.size = n
        self.array = [None] * n # Create an empty array with size n 
        self.middle = math.floor(n / 2)
        self.top1 = 0
        self.top2 = math.floor(n/2)
    
    def push1(self, x):
        if (self.top1 < self.middle):
            self.array[self.top1] = x
            self.top1 = self.top1 + 1
        else:
            return "Stack is OverFlow"

    def push2(self, x):
        if(self.top2 < self.size):
            self.array[self.top2] = x
            self.top2 = self.top2 + 1
        else:
            return "Stack is OverFlow"
        
    def pop1(self):
        if(not(self.top1 == 0)):
            x = self.array[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            return "Stack is UnderFlow"
        
    def pop2(self):
        if(not(self.top1 == self.size)):
            x = self.array[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            return "Stack is UnderFlow"


if __name__ == "__main__":
    obj = Stack(5)      # Object with array of 5 element size
    obj.push1(10)
    obj.push2(20)
    obj.push1(30)
    obj.push2(40)
    obj.push1(100) # Stack OverFlow Exception
    obj.push2(200) 



