# Implementation of Stack (Traversal, insert, delete, and search)
from collections import deque

class Stack():
    def __init__(self, *elements):
        self._elements = deque(elements)
    
    def push(self, value):
        # In stack push happens in last stack value (first element of dequeue)
        self._elements.appendleft(value)

    def pop(self):
        # In stack pop happens for first stack value (first element of dequeue)
        if self.is_empty():
            return "Stack is Empty"
        
        return self._elements.popleft()
    
    def __len__(self):
        return len(self._elements)
    
    def is_empty(self):
        return len(self._elements) == 0
    
    def top(self):
        # Returns top most element of stack 
        return self._elements[0]
    
    # Delete middle element 
    def delete_at_midddle(self, stack: deque[int], middle: int) -> deque[int]:
        # Base Condition:
        if (middle == 0):
            stack.popleft()
            return stack
        
        # Hypothesis:
        temp = stack.popleft()
        self.delete_at_midddle(stack, middle - 1)

        # Induction: Add the popped values 
        stack.appendleft(temp)

        return stack

    # Traverse through each element   
    def __iter__(self):
        for item in self._elements:
            yield item 


if __name__ == "__main__":
    stack_array = Stack()
    stack_array.push(10)
    stack_array.push(20)
    stack_array.push(30)
    stack_array.push(40)
    stack_array.push(50)
    stack_array.push(60)
    stack_array.push(70)
    stack_array.push(80)
    stack_array.push(90)
    # Comprehensions 
    stack_items = deque([item for item in stack_array])
    print(stack_items)

    # Delete middle element of stack 
    middle = len(stack_array) // 2 - 1 if len(stack_array) % 2 == 0 else len(stack_array) // 2
    stack_result = stack_array.delete_at_midddle(stack_items, middle)
    stack_values = [item for item in stack_result]
    print("Stack after deleting middle element")
    print(stack_values)
