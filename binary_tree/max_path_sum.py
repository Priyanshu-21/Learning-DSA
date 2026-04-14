# Implementation of max_path sum in binary Tree
# Approach Recursive post - order traversal 
# Pattern: Traversal (post-order) + global maximum (left + right + root.val) 
# and return max(root.val + max(left, right), root.val)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maximum = int(-10**5) # Highest negative value, to store maximum value

    def solve_maxPathSum(self, root):
        # Base Condition: 
        if (root == None):
            return 0
        
        # Traversal: Post order (Left-Right-Root)
        left = self.solve_maxPathSum(root.left)
        right = self.solve_maxPathSum(root.right)

        # Update Maximum value (left, root, right)
        left, right = max(0, left), max(0, right)
        self.maximum = max(self.maximum, left + root.val + right)
        
        # Return maximum path result 
        return max(root.val + max(left, right), root.val)


    def maxPathSum(self, root: TreeNode) -> int:
        # Recursive Approach (Using post-order Traversal)

        self.solve_maxPathSum(root)

        # maximum stores max path value in tree
        return self.maximum
    

root = TreeNode(10)
root.left = TreeNode(2)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)

root.right = TreeNode(10)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

# Call function to get maximum path sum 
sol = Solution()
result = sol.maxPathSum(root)

print(f'Maximum Path sum of Tree is {result}')