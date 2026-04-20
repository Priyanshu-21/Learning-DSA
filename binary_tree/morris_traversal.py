# Implementation of Morris Traversal (Threaded Binary Tree)

class TreeNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left, self.right = left, right

class Solution():
    def morris_traversal(self, root):
        # Morris Traversal: 3 Cases approach 
        inorder = []
        current = root # current node to be tracked 

        while (current != None):
            # Case 1: current.left = Null, so at root, print it and move current to right 
            if (current.left == None):
                inorder.append(current.data)
                current = current.right 
            
            else:
                # Case 2: Goto right most part of tree and make thread to current node.
                prev = current.left 
                while (prev.right != None and prev.right != current):
                    # Move previous to right 
                    prev = prev.right
                
                # Case 3: when right part of node it's connection to current 
                if (prev.right == None):
                    prev.right = current
                    current = current.left

                else:
                    # Unlink the prev.right thread 
                    prev.right = None

                    # Add current into list, as it's root node 
                    inorder.append(current.data)
                    current = current.right 

        # Return in-order Traversal value 
        return inorder

    def morris_traversal_pre_order(self, root):
        # Morris Traversal Pre-Order (Root, Left, Right)
        preorder = []
        current = root # Current pointer to make threaded binary tree 
        
        while (current != None):
            # Case 1: When current.left == None, print root and move right 
            if (current.left == None):
                preorder.append(current.data)
                current = current.right
            
            else: 
                # Case 2: When prev.right = None, change it to current and print current 
                prev = current.left 
                while (prev.right != None and prev.right != current):
                    prev = prev.right
                
                if (prev.right == None):
                    prev.right = current
                    preorder.append(current.data)
                    current = current.left 
                
                else:
                    # Case 3: Unthread binary link, and move to right tree part 
                    prev.right = None 
                    current = current.right 
        
        # Return pre-order Traversal 
        return preorder


root = TreeNode(8)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.right = TreeNode(7)
root.left.right.right = TreeNode(10)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
root.right.left.left= TreeNode(6)

sol = Solution()

print(f"In-order Morris Traversal of Tree: {sol.morris_traversal(root)}")

print(f"Pre-Order Morris Traversal of Tree: {sol.morris_traversal_pre_order(root)}")