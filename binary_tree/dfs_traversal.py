# DFS Binary Tree Traversal using 1 Stack iterative approach 
from collections import deque

class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right

class Traversal():
    def in_order_traversal(self, root):
        # Iterative approach (Left, root, right)
        stack_1 = deque()
        res = []
        node = root 
        while (stack_1 or node):
            # Travel to left sub-tree, until null node. 
            while (node != None):
                stack_1.append(node)
                node = node.left
            
            # We are at root, print it
            top = stack_1.pop()
            res.append(top.data)

            # Mode to node right, position 
            node = top.right
        
        return res
    
    def pre_order_traversal(self, root):
        # Iterative approach (root, left, right)
        stack_2 = deque()
        res = []

        # Make entry of root in stack 
        stack_2.append(root)
        while (stack_2):
            # Take out node and find it's left, right child 
            node = stack_2.pop()
            res.append(node.data)

            if (node.right != None):
                # Save entry of node right 
                stack_2.append(node.right)
            
            if (node.left != None):
                # Save entry of node left 
                stack_2.append(node.left)
        
        return res
    
    def post_order_traversal(self, root):
        # Iterative approach (left, right, root)
        stack_3 = deque()
        res = []

        # Approach Traverse (Root -> Right -> Left) and then reverse the order 
        stack_3.append(root)
        while (stack_3):
            node = stack_3.pop()
            res.append(node.data)

            if (node.left != None):
                stack_3.append(node.left)
            
            if (node.right != None):
                stack_3.append(node.right)
        
        # Reverse list to get result
        return res[::-1]



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
sol = Traversal()

res_inorder = sol.in_order_traversal(root)
res_preorder = sol.pre_order_traversal(root)
res_postorder = sol.post_order_traversal(root)

print(f"In-Order Traversal: {res_inorder}")
print(f"Pre-Order Traversal: {res_preorder}")
print(f"Post-Order Traversal: {res_postorder}")
