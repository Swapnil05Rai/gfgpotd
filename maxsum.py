class Solution:
    def maxLevelSum(self,root):
        maxi = float('-inf')
        q = [root]
        
        while q:
            n = len(q)
            sum = 0
            for i in range(n):
                p = q.pop(0)
                sum += p.data
                
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            maxi = max(maxi, sum)
            
        return maxi

"""This is a solution to the problem of finding the level in a binary tree that has the maximum sum of node values.

The maxLevelSum function takes the root node of the binary tree as input and returns the level with the maximum sum.

The function starts by initializing a queue with the root node, and a variable maxi to hold the maximum sum found so far.

Then it enters a loop where it processes the nodes in the queue level by level. At the beginning of each iteration of the loop, the number of nodes at the current level is determined by getting the size of the queue.

Then a variable sum is initialized to zero to hold the sum of node values at the current level. Next, each node at the current level is removed from the queue one by one, its value is added to the sum, and its children (if any) are added to the queue.

After processing all the nodes at the current level, the sum variable holds the sum of node values at that level, which is then compared with the current maximum maxi, and maxi is updated if sum is greater.

Finally, the function returns maxi, which holds the maximum sum found in any level of the binary tree."""
