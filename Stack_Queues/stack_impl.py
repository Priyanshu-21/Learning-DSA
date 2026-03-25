from collections import deque

# Revision of stack implementation using Deque
class Stack(deque):
    def __init__(self, *elements):
        self._elements = deque(elements)
    
    def build_stack(self, element):
        # Add elements in last-in format 
        self._elements.appendleft(element)
    
    def pop_stack(self):
        # Pop elemtns in first-out format
        self._elements.popleft()
        return self._elements
    
    def reverse_stack(self, stack: deque[int]) -> deque[int]:
        # Base Condition:
        if (len(stack) == 0):
            return stack
        
        # Hypothesis:
        temp = stack.pop()
        self.reverse_stack(stack)

        # Induction:
        stack.appendleft(temp)

        return stack
    
    # Traversal of stack elements 
    def __iter__(self):
        for ele in self._elements:
            yield ele


if __name__ == "__main__":
    stk = Stack()
    stk.build_stack(80)
    stk.build_stack(70)
    stk.build_stack(60)
    stk.build_stack(40)
    stk.build_stack(30)
    stk.build_stack(20)
    stk.build_stack(10)
    print(f"Elements in the stack: \n")
    stack_element = [ele for ele in stk]
    stack_element = deque(stack_element)
    print(stack_element)
    # Reverse stack elements using recursion
    result = stk.reverse_stack(stack_element)
    print(f"Stack Reverse Elements: \n{result}")
