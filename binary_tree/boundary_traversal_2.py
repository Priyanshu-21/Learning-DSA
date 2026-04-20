# Boundary Traversal: Iterative approach (Left + Right Part) + Morris Traversal (Leave Nodes)

class TreeNode():
    def __init__(self, data, left= None, right= None):
        self.data = data
        self.left, self.right = left, right
    

class Solution():
    def is_leaf(self, root):
        return True if (root.left == None and root.right == None) else False
    

    def left_tree(self, root, result):
        current = root

        while (self.is_leaf(current) != True):
            # Append current node in result and move to left or right part 
            result.append(current.data)

            if (current.left != None):
                current = current.left
            
            elif (current.right != None):
                current = current.right


    def right_tree(self, root, right_result):
        current = root 

        while (self.is_leaf(current) != True):
            # Append the right_result in node and move to right or left part
            right_result.append(current.data)

            if (current.right != None):
                current = current.right 
            
            elif (current.left != None):
                current = current.left 


    def get_leave_nodes(self, root, result):
        current = root

        while (current != None):
            # Case 1: 
            if (current.left == None):
                if (current.right == None):
                    result.append(current.data)
                current = current.right
            
            else: 
                # Case 2: Make Threaded binary Tree, 
                prev = current.left 
                while (prev.right != None and prev.right != current):
                    prev = prev.right
                
                # When prev.right == None 
                if (prev.right == None):
                    prev.right = current
                    current = current.left 
                
                else: 
                    if (prev.left == None):
                        result.append(prev.data)

                    prev.right = None # Un-thread the binary Tree
                    current = current.right

            
    def boundary_traversal(self, root):
        # Iterative Approach: Left + Right (except) Leave Node 
        # Leave Node: - Morris Traversal 

        result = []
        result.append(root.data) # Append root of node first in result 

        if (root.left != None):
            self.left_tree(root.left, result)
        
        # Leave Nodes of binary Tree, Morris Traversal 
        self.get_leave_nodes(root, result)

        right_result = []
        if (root.right != None):
            self.right_tree(root.right, right_result)
        
        result = result + right_result[::-1] # Reverse order of right part 
        return result


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
tree.right.right.right = TreeNode(4)

sol = Solution()
print(f"Boundary Traversal of Tree: {sol.boundary_traversal(tree)}")