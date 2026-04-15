from collections import deque, OrderedDict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        # Iterative Level order Traversal + line concept to store node for level 
        queue = deque()
        map = OrderedDict() # Ordered dictionary 
        result = []
        # Append root value with level, line and node 
        queue.append((0, 0, root))

        while queue:
            # Take out node, level and line value 
            level, line, node = queue.popleft() # Queue DS 
            
            # Append line: node value to map 
            map.setdefault(line, []).append(node.val)
            

            if (node.left != None):
                # Push node value to queue
                queue.append((level + 1, line - 1, node.left))
            
            if (node.right != None):
                # Push node value to queue
                queue.append((level + 1, line + 1, node.right))
            
        # Update key values to result list 
        for _, value in sorted(map.items()):
            result.append(sorted(value))

        return result
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.verticalTraversal(root)

print(f"Vertical order Traversal of tree: {result}")