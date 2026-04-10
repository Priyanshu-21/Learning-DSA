# Introduction to Level Order Traversal in Trees 
class Tree():
    def __init__(self, data, left= None, right= None):
        self.data = data 
        self.left, self.right = left, right

class Solution:
    def level_order_traversal(self, root, level, res):
        # Base condition:
        if (root == None):
            return 
        
        if (len(res) <= level):
            res.append([])
            
        # Register element at level for the  root
        res[level].append(root.data)
        
        # Move to left child with level + 1
        self.level_order_traversal(root.left, level + 1, res)
        
        # Move to right child with level + 1
        self.level_order_traversal(root.right, level + 1, res)
        
        
    def levelOrder(self, root):
        # code here
        level = 0 
        res = []
        
        self.level_order_traversal(root, level, res)
        
        return res


root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
root.left.left = Tree(40)
root.left.right = Tree(50)

sol = Solution()
result = sol.levelOrder(root)

print(result)