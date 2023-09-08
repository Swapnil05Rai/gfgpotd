class Solution:
    def inorder(self, root, v):
        if not root:
            return
        self.inorder(root.left, v)
        v.append(root.data)
        self.inorder(root.right, v)
        
    def fill_it(self, root, v, ind):
        if not root:
            return
        self.fill_it(root.left, v, ind)
        root.data = v[ind[0]]
        ind[0]+=1
        self.fill_it(root.right, v, ind)

    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        # code here
        v = []
        # STEP 1 : Do inorder traversal and store each node data in array or list
        self.inorder(root, v) 
        # STEP 2 : Sort the array or List
        v.sort() 
        ind = [0]
        # STEP 3: Update the Binary tree to make it BST
        self.fill_it(root, v, ind) 
        return root
