# Approach & Implementation to find tree maximum depth 
from collections import deque
class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right

class Solution:
    # helper function of recursive approach 
    def solve_depth(self, root) -> int:
        # Base condition 
        if (root == None):
            return 0

        lc = self.solve_depth(root.left)
        rc = self.solve_depth(root.right)

        return max(lc, rc) + 1

    # Recursive Approach #1
    def maxDepth(self, root: TreeNode) -> int:
        # Maxium depth using recursive approach 
        # Edge Case: 
        if (root == None):
            return 0
        
        # Return depth of longest path of a tree
        result = self.solve_depth(root)
        return result
    
    # Iterative Approach #2
    def height(self, root):
        # code here
        # Iterative Level order Traversal approach 
        queue = deque()
        res = []
    
        # Edge case: 
        if (root == None):
            return 0
        
        # add root to queue 
        queue.append((root, 0)) # Appending root node and level 
        
        while queue:
            # Take out node and add it's left and right child in Queue
            # And add node to result level list 
            node, level = queue.popleft()
            
            if (len(res) <= level):
                res.append([])
            
            res[level].append(node.data)
            
            # Goto left and right child of queue
            if (node.left != None):
                queue.append((node.left, level + 1))
                
            if (node.right != None):
                queue.append((node.right, level + 1))
                    
        return len(res)
     


# Structure of Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Print results for this tree in each traversal 
sol = Solution()

print(sol.height(root))