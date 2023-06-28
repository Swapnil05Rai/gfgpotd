def maxDepth(self,root):
        if not root:return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
