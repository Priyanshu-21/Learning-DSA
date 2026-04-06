# Representation of Binary Tree (Structure + Creation of Binary Tree)

class Tree():
    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None
    

class BinaryTree():

    # In-order Traversal (Depth First Search)
    def in_order_traversal(self, root, results: list[int]):

        # Base Case: 
        if (root == None):
            return 
        
        # Move to left node 
        self.in_order_traversal(root.left_child, results)

        # In middle node, print node data 
        results.append(root.data)

        # Move to right node 
        self.in_order_traversal(root.right_child, results)

        return results

    def pre_order_traversal(self, root, results: list[int]):

        # Base Condition 
        if (root == None):
            return 
        
        # Traverse the root node 
        results.append(root.data)
        
        # Taverse to left child 
        self.pre_order_traversal(root.left_child, results)

        # Traverse to right child 
        self.pre_order_traversal(root.right_child, results)

        return results
    
    def post_order_traversal(self, root, results: list[int]):
        
        # Base condition 
        if (root == None):
            return 
        
        # Traverse to left child 
        self.post_order_traversal(root.left_child, results)
        
        # Traverse to right child
        self.post_order_traversal(root.right_child, results)

        # Traverse to root 
        results.append(root.data)

        return results


binary_tree = BinaryTree()
root = Tree(2)
root.left_child = Tree(1)
root.right_child = Tree(3)
root.left_child.left_child = Tree(4)
root.left_child.right_child = Tree(5)

# In-order Traversal 
print(f"Inorder Traversal of Binary Tree:")
results = binary_tree.in_order_traversal(root, [])
print(results)

print(f"Pre-Order Traversal of Binary Tree:")
results = binary_tree.pre_order_traversal(root, [])
print(results)

print(f"Post-Order Traversal of Binary Tree:")
results = binary_tree.post_order_traversal(root, [])
print(results)


