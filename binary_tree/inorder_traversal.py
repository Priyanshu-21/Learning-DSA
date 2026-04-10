# In-order Traversal using 1 stack approach 

from collections import deque

class TreeNode():
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.left, self.right = left, right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:

        # In-Order Traversal with 1 Stack iterative approach 
        stack_1 = deque()
        result = []
        # Edge case: - 
        if root == None:
            return result

        # Pointer node keep tracking nodes details 
        node = root
        
        while stack_1 or node:
            # Move to left until finding null 
            while node != None:
                stack_1.append(node)
                node = node.left
                
            # Print node and move to right
            top = stack_1.pop()
            result.append(top.val)

            # Move right 
            node = top.right
 
        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)

sol = Solution()
res = sol.inorderTraversal(root)

print(res)