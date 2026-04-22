# Introduction to inserting a node in Binary Search Tree
class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right


class Solution:        
    def insert(self, root, key):
        # Recursive Insert approach 
        # Base condition 
        if (root == None):
                
            return TreeNode(key)
        
        if (key > root.data):
            # Move right of binary tree 
            root.right = self.insert(root.right, key)
        
        elif (key < root.data):
            root.left = self.insert(root.left, key)
        
        return root
    
    def inorder_traversal(self, root, result):
        # Base condition: 
        if (root == None):
            return 
         
        self.inorder_traversal(root.left, result)
        result.append(root.data)
        self.inorder_traversal(root.right, result)

        return result


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

sol = Solution()
key = 4
new_bst = sol.insert(root, key)
res = sol.inorder_traversal(new_bst, [])

print(f"BST after inserting {key}: {res}")

