def goodSubtrees(self, root, k):
        
        ans = 0
        def walk(node):
            nonlocal ans
            if not node:
                return set()
            left = walk(node.left)
            right = walk(node.right)
            r = left.union(right).union({node.data})
            if len(r) <= k:
                ans += 1
            return r
        walk(root)
        return ans
      
"""This is a solution to the problem of finding the number of good subtrees in a binary tree. A subtree is considered good if the number of distinct values in the subtree is less than or equal to k.

The function goodSubtrees takes two parameters: root, which is the root node of the binary tree, and k, which is the maximum number of distinct values allowed in a good subtree.

The algorithm performs a depth-first search on the binary tree, starting from the root node. At each node, it recursively walks the left and right subtrees, and collects the set of distinct values in those subtrees, along with the value at the current node. It then checks if the size of the set is less than or equal to k, and if so, increments the ans counter.

The function returns the ans counter, which is the total number of good subtrees in the binary tree."""
