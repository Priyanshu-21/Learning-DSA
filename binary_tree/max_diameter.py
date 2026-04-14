# Implementation of diameter of binary Tree

class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data 
        self.left, self.right = left, right

# Diameter of Binary Tree
class BinaryTree():
    def __init__(self):
        self.max_diameter = 0

    def solve_diameter(self, root):
        # Base Condition:
        if (root == None):
            return 0
        
        # calculate height of left, right sub-tree
        left_height = self.solve_diameter(root.left)
        right_height = self.solve_diameter(root.right)

        # For each sub-tree calculate it's diameter (editing in golbal variable)
        self.max_diameter = max(self.max_diameter, left_height + right_height)

        # Return each node height 
        return max(left_height, right_height) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.solve_diameter(root)

        return self.max_diameter


root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)

sol = BinaryTree()

max_diameter = sol.diameterOfBinaryTree(root)
print(f'Maximum diameter of a Tree: {max_diameter}')

