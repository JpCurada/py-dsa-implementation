class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # TODO: Initialize empty binary search tree
        # - Root node is None initially
        self.root = None

    def create_binary_tree(self):
        # TODO: Reset binary tree to empty state
        # - Set root to None
        self.root = None
        return True

    def insert(self, data):
        # TODO: Insert new node with data
        # - Use recursive helper function
        # - Handle duplicate values by not inserting
        
        # Create recursive helper function
        def _insert_recursive(root, data):
            # Base case: if root is None, create new node
            if root is None:
                return TreeNode(data)
                
            # Recursively insert into left or right subtree
            if data < root.data:
                root.left = _insert_recursive(root.left, data)
            elif data > root.data:
                root.right = _insert_recursive(root.right, data)
            # If data is equal to root.data, don't insert (handle duplicates)
                
            return root
            
        # Call helper function starting at root
        self.root = _insert_recursive(self.root, data)
        return True

    def delete(self, data):
        # TODO: Delete node with given data
        # - Use recursive helper function
        # - Handle cases: leaf node, node with one child, node with two children
        
        # Create recursive helper function
        def _delete_recursive(root, data):
            # Base case: if root is None, data not found
            if root is None:
                return None, False
                
            # Find the node to delete
            if data < root.data:
                root.left, deleted = _delete_recursive(root.left, data)
                return root, deleted
            elif data > root.data:
                root.right, deleted = _delete_recursive(root.right, data)
                return root, deleted
            else:
                # Node found - handle deletion cases
                
                # Case 1: Leaf node (no children)
                if root.left is None and root.right is None:
                    return None, True
                    
                # Case 2: Node with only one child
                elif root.left is None:
                    return root.right, True
                elif root.right is None:
                    return root.left, True
                    
                # Case 3: Node with two children
                # Find inorder successor (smallest node in right subtree)
                successor = root.right
                while successor.left is not None:
                    successor = successor.left
                    
                # Copy successor data to root
                root.data = successor.data
                
                # Delete the successor
                root.right, _ = _delete_recursive(root.right, successor.data)
                return root, True
                
        # Call helper function starting at root
        self.root, deleted = _delete_recursive(self.root, data)
        return deleted, "Element deleted successfully" if deleted else "Element not found"

    def display_binary_tree(self):
        # TODO: Create string representation of binary tree
        # - Use inorder traversal helper function
        # - Return list of elements in sorted order
        
        elements = []
        
        # Inorder traversal helper function
        def _inorder_traversal(root):
            if root:
                _inorder_traversal(root.left)
                elements.append(str(root.data))
                _inorder_traversal(root.right)
                
        # Perform inorder traversal
        _inorder_traversal(self.root)
        
        if not elements:
            return "Empty tree"
            
        return "Inorder: " + " -> ".join(elements)

    def display_tree_structure(self):
        # TODO: Create string representation of tree structure
        # - Use recursive helper function
        # - Show tree with indentation to indicate levels
        
        if self.root is None:
            return "Empty tree"
            
        result = []
        
        # Helper function to build tree string
        def _display_recursive(node, level, prefix):
            if node is not None:
                # Add current node
                result.append(" " * (level * 4) + prefix + str(node.data))
                
                # Process children
                if node.left is not None or node.right is not None:
                    # Left child
                    _display_recursive(node.left, level + 1, "L: " if node.left else "   ")
                    # Right child
                    _display_recursive(node.right, level + 1, "R: " if node.right else "   ")
                    
        # Start recursive display
        _display_recursive(self.root, 0, "")
        
        return "\n".join(result)