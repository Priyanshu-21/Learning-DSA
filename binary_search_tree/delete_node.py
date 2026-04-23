# Implementation of Deleting node in a Binary Search Tree: 

class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right

class Solution():
    def is_leaf(self, root):
        return True if (root.left == None and root.right == None) else False
    
    def inorder_successor(self, root):
        # Find minimum value in right - tree, left part 
        while (root.left != None):
            root = root.left

        return root

    def delete_node(self, root, value):
        # Recursive approach:
        # Base condition: When value not in BST 
        if (root == None):
            return None
        
        # Left and right sub-tree 
        if (value < root.data):
            root.left = self.delete_node(root.left, value)
        
        elif (value > root.data):
            root.right = self.delete_node(root.right, value)
        
        else: 
            # value == root.data 
            # Here, we need to delet node of Binary Tree and maintain BST properties 
            # Case 1: Node has no children (Leaf node)
            if (self.is_leaf(root)):
                return None
            
            # Case 2: Node has 1 children (either left or right subtree)
            elif (root.left == None):
                return root.right
            
            elif (root.right == None):
                return root.left 
            
            # Case 3: Node has 2 children, find in-order successor of the node in right subtree  
            else: 
                successor = self.inorder_successor(root.right)
                # Replace successor and root values 
                root.data = successor.data

                # Check for case 1 and 2 again, 
                root.right = self.delete_node(root.right, successor.data)
        
        # Return the head of binary Tree
        return root
    
    def tree_traversal(self, root):
        # Morris In-order Traversal 
        current = root # current pointer to keep track of node in tree
        result = []
        while (current != None):
            # Case 1: if current.left == None, left part (print node) & move right 
            if (current.left == None):
                result.append(current.data)
                current = current.right
            else: 
                # Case 2: Make threaded BT with prev.right = current and move current to left 
                prev = current.left 
                while (prev.right != None and prev.right != current):
                    prev = prev.right
                
                if (prev.right == None):
                    prev.right = current
                    current = current.left 
                
                # prev.right == current
                else: 
                    # Case 3: Thread already there, unthread it and print node & move right 
                    prev.right = None 
                    result.append(current.data)
                    current = current.right
        
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(5)
root.right.right.left.left = TreeNode(4)
root.right.right.left.right = TreeNode(7)
root.right.right.right = TreeNode(11)
root.right.right.right.left = TreeNode(9)
root.right.right.right.right = TreeNode(12)

sol = Solution()
res = sol.delete_node(root, 12)
result = sol.tree_traversal(res)
print(f"Binary Tree after Deletion: {result}")

