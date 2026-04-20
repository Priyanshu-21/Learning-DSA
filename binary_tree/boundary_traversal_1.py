# Introduction to boundary Traversal
# Approach 1: using Recursion; Idea: Left Part, Leaf Node's and right part in reverse order 

class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right

class Solution():
    def is_leaf(self, root) -> bool:
        return True if (root.left == None and root.right == None) else False
    

    def tree_right(self, root: TreeNode, result): 
        # Base condition 
        if (root == None or self.is_leaf(root) == True):
            return 
        
        # Move right part of tree, if not null otherwise move to left part 
        if (root.right != None):
            self.tree_right(root.right, result)

        elif (root.left != None):
            self.tree_left(root.left, result)

        # Append node in result (already in reverse order)
        result.append(root.data)


    def get_leave_nodes(self, root, result):
        # Base condition 
        if (root == None):
            return 
        
        if (self.is_leaf(root) == True):
            # Pointer at leaf node 
            result.append(root.data)

        # Move to left and right part of tree
        self.get_leave_nodes(root.left, result)

        self.get_leave_nodes(root.right, result)
        

    def tree_left(self, root, result):
        # Base condition: if node == None or node != leaf node 
        if (root == None or self.is_leaf(root) == True):
            return 
        
        # Add value of the node 
        result.append(root.data)

        if (root.left != None):
            self.tree_left(root.left, result)
        
        elif (root.right != None):
            self.tree_left(root.right, result)


    def boundary_traversal_recursive(self, root: TreeNode):
        result = []
        # Append root node value
        result.append(root.data)

        # Left Part of Binary Tree
        if (root.left != None):
            self.tree_left(root.left, result)

        # Get all leaf Node of Binary Tree
        if (root.left != None or root.right != None):
            self.get_leave_nodes(root, result)

        # Right Part of Binary Tree
        if (root.right != None):
            self.tree_right(root.right, result)
        
        return result 


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.left.right.left = TreeNode(8)
tree.left.right.right = TreeNode(9)

tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
'''tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
tree.right.right.right = TreeNode(4)'''

sol = Solution()

res = sol.boundary_traversal_recursive(tree)
print(f"Boundary Traversal of Tree: {res}")