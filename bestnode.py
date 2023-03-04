    def bestNode(self, N : int, A : List[int], P : List[int]) -> int:
        from collections import defaultdict
        g = defaultdict(list)
        for i, parent in enumerate(P):
            g[parent].append(i+1)
            
     
        ans = float('-inf')
        def dfs(n):
            nonlocal g, ans, A
            if not g[n]:
                ans = max(ans, A[n-1])
                return A[n-1], A[n-1]
            
            maxv, minv = float('-inf'), float('inf')
            for nxt in g[n]:
                ma, mi = dfs(nxt)
                maxv = max(maxv, A[n-1]-mi)
                minv = min(minv, A[n-1]-ma)
            ans = max(ans, maxv)
            return maxv, minv
        
        dfs(1)
        return ans
      
"""This is a Python solution for a problem that involves finding the best node in a tree. Here is how the code works:

First, the code constructs a tree using a defaultdict where the keys are parent nodes and the values are child nodes.
Then, it defines a function called dfs that takes in a node n and recursively traverses its children nodes to find the best node.
If the current node is a leaf, the function returns the value of the node, A[n-1], twice since it is both the maximum and minimum value in the subtree.
If the current node has children, the function calls dfs on each child and returns the maximum and minimum values in the subtree.
Finally, the function calculates the maximum difference between the current node and its children and updates the answer if necessary.
The function bestNode takes in the number of nodes N, a list A containing the values of the nodes, and a list P containing the parent node for each node. It returns the value of the best node in the tree.




"""
