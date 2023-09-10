def insert(self,root, Key):
        # code here
        if not root:
            return Node(Key)  # If the tree is empty, return a new node with value Key.

        current = root
        while True:
            if Key < current.data:
                if current.left is None:
                    current.left = Node(Key)
                    break
                else:
                    current = current.left
            elif Key > current.data:
                if current.right is None:
                    current.right = Node(Key)
                    break
                else:
                    current = current.right
            else:
                # If K is already present in the BST, do nothing.
                break
    
        return root
