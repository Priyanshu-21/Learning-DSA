# Implementation of post order traversal using 2 stack approach 
from collections import deque

class TreeNode():
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root) -> list[int]:
        # Stack Iterative Approach using 2 stacks
        stack_1 = deque()
        stack_2 = deque()
        results = []
        # Push root node to stack #1
        stack_1.appendleft(root)
        

        while (len(stack_1) != 0):
            # Pop item from stack_1 and add item's left and right node details 
            node = stack_1.popleft()
            
            if (node.left != None):
                stack_1.appendleft(node.left)

            if (node.right != None):
                stack_1.appendleft(node.right)
            
            # Add item to stack 2 (Stack 2 will have results stored in post-order)
            stack_2.appendleft(node)
        
        # Copy elements from stack_2 to list 
        while stack_2:
            results.append(stack_2.popleft().val)
        
        return results
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)

sol = Solution()
res = sol.postorderTraversal(root)

print(res)
