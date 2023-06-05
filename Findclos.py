def minSearch(self, root, k ,l):
        if root is None:
            return l
        if root.data == k:
            return [0]
        l.append(abs(k-root.data))
        if k>root.data:
            return self.minSearch(root.right, k, l)
        else:
            return self.minSearch(root.left, k, l)
            
    def minDiff(self,root, K):
        l = []
        l = self.minSearch(root,k,l)
        return min(l)
