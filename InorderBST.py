class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        successor = None
        
        while root:
            if x.data < root.data:
                # Update successor to the current node and move to the left subtree
                successor = root
                root = root.left
            elif x.data > root.data:
                # Move to the right subtree
                root = root.right
            else:
                # Node x is found
                # If x has a right subtree, find the leftmost node in that subtree
                if root.right:
                    successor = root.right
                    while successor.left:
                        successor = successor.left
                break
                
        return successor
