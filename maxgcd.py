class Solution:
    def __init__(self):
        self.max=float('-inf')
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)
    def maxGCD(self, root):
        if not root or (not root.left and not root.right):
            return 0
        q = []
        q.append(root)
        res = 0
        while q:
            flag = False
            cur = q.pop(0)
            curr = 0
            if cur.left and cur.right:
                curr = self.gcd(cur.left.data, cur.right.data)
                flag = True
            if curr >= self.max and flag:
                self.max = curr
                res = cur.data
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res

ob = Solution()
"""The problem is to find the node whose two immediate children has the maximum GCD in a binary tree. 
To solve this problem, you can use a depth-first search (DFS) or Breadth First Search (BFS) algorithm to traverse the tree and find the GCD of each pair of siblings. 
Then you would need to compare the GCDs of all pairs and find the maximum GCD. Finally, you would need to return the node whose children have the maximum GCD.
It's important to check if the tree is empty and if no such pair of siblings found, return 0 as per the question.
The provided python code uses BFS to traverse the tree and find the max GCD for the siblings and return the node whose two immediate children has the maximum GCD."""
