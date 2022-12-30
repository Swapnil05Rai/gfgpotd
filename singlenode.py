class Solution:
    def helper(self, root):
        # if the current node is a leaf node, increment the count and return True and the value of the node
        if not root.left and not root.right:
            self.count += 1
            return True, root.data
        
        # initialize variables to store the return values of the recursive calls
        rflag, rval, lflag, lval = True, root.data, True, root.data
        
        # call the helper function recursively on the left and right children
        if root.left: 
            lflag, lval = self.helper(root.left)
        if root.right: 
            rflag, rval = self.helper(root.right)

        # check whether the current subtree is single-valued
        if lflag and rflag and lval==rval and root.data==lval and root.data==rval:
            # if it is, increment the count and return True and the value of the root node
            self.count += 1
            return True, root.data
        # if it is not, return False and the value of the root node
        return False, root.data

    def singlevalued(self, root):
        # initialize the count variable to 0
        self.count = 0
        # call the helper function on the root node
        self.helper(root)
        # return the count
        return self.count
