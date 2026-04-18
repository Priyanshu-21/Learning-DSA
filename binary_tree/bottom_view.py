# Implementation of bottom view of Binary Tree (Using Iterative Approach)
from collections import deque

# Tree Structure 
class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right

class Solution():
    def bottom_view(self, root: TreeNode):
        # Iterative BFS (level order Traversal) + vertical order approach 
        queue = deque()
        map = dict() # Map to store node with vertical line 
        result = []
        
        queue.append((0, 0, root))
        
        while (queue):
            # each queue index has level, line and node information 
            level, line, node = queue.popleft()

            # Move to node left and right if not null 
            if (node.left != None):
                queue.append((level + 1, line - 1, node.left))
            
            if (node.right != None):
                queue.append((level + 1, line + 1, node.right))
            
            # Put node values to map 
            map[line] = []
            map[line].append(node.data)
        
        # Now map has element all node store in line order 
        # To get bottom view, we need to get value's last item in each key 

        for _, value in sorted(map.items()):
            result.append(value[-1]) # Append each key: values last element 
        
        return result


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)
root.right.left = TreeNode(90)
root.right.right = TreeNode(100)

sol = Solution()
result = sol.bottom_view(root)

print(f"Bottom View of tree: {result}")
