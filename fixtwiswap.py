class Solution:

    def correctBST(self, root):

        """

        Given the root of a BST with two nodes swapped, fixes the BST by swapping them back.

        """

        # Initialize pointers and predecessor

        first, second, prev = None, None, Node(float('-inf'))

 

        # Helper function to traverse the BST in order

        def inorder_traversal(node):

            nonlocal first, second, prev

 

            if not node:

                return

 

            inorder_traversal(node.left)

 

            # Check if current node violates the BST property

            if not first and prev.data > node.data:

                first = prev

            if first and prev.data > node.data:

                second = node

 

            prev = node

 

            inorder_traversal(node.right)

 

        # Traverse the tree in order to identify the misplaced nodes

        inorder_traversal(root)

 

        # Swap the values of the misplaced nodes

        first.data, second.data = second.data, first.data

        return root
