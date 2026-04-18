# Introduction to top-view of binary Tree
from collections import deque

class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right

class Solution():
    def top_view_binary_tree(self, root: TreeNode):
        # Iterative level order traversal + vertical order traversal 
        queue = deque()
        map = dict() # Map to store line: node values 

        queue.append((0, 0, root))

        while queue: 
            # Pop queue element and goto node left and right 
            level, line, node = queue.popleft()

            # Left-part of tree
            if (node.left != None):
                queue.append((level + 1, line - 1, node.left))

            # right-part of tree
            if (node.right != None):
                queue.append((level + 1, line + 1, node.right))

            # Check if popped node present in map, if yes skipped (already seen top-most node)
            if (line not in map):
                map[line] = node.data
        
        return map

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)
root.right.left = TreeNode(90)
root.right.right = TreeNode(100)

sol = Solution()
result = sol.top_view_binary_tree(root)

print(f"Top View of tree: {result}")

