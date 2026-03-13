# Introduction to Stack Dynamic Data Set 

# 1. Implementation using list 
class Stack: 
    def pushElement(stack, x):
        if (len(stack) == 5):
            print("Stack is Overflow")
            return
        
        stack.append(x)
        print(stack)

    def popElement(stack):
        if (len(stack) == 0):
            print("Stack UnderFlow")
            return
        else:
            stack.pop() # Pop the last element in list 
            print(stack)

stack = []
result = Stack.pushElement(stack, 2)
print(result) 

# 2. Implementation using collections.dequeue
from collections import deque

class Stack:
    def push(stack, x):
        if (len(stack) == 4):
            print("Stack OverFlow")
            return
        else:
            stack.append(x)
            print(stack)
    
    def pop(stack):
        if (len(stack) == 0):
            print("Stack UnderFlow")
            return
        else:
            stack.pop()
            print(stack)

stack = deque()
Stack.push(stack, 10)
Stack.push(stack, 20)
Stack.push(stack, 30)
Stack.push(stack, 40)
Stack.push(stack, 50) # Stack will be overflow

Stack.pop(stack)
Stack.pop(stack)
Stack.pop(stack)
Stack.pop(stack)
Stack.pop(stack) # Stack will be underflow 

