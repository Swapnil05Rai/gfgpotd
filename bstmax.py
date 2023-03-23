class Solution:
    def maxDifferenceBST(self,root, target):
        #code here
        def dfs(node, path_sum, target):
            if not node:
                return None, float('-inf')

            path_sum += node.data
            if node.data == target:
                return node, path_sum

            if node.data > target:
                return dfs(node.left, path_sum, target)
            else:
                return dfs(node.right, path_sum, target)

        def leaf_sum(node, curr_sum):
            if not node:
                return float('inf')

            if not node.left and not node.right:
                return curr_sum + node.data

            return min(leaf_sum(node.left, curr_sum + node.data), leaf_sum(node.right, curr_sum + node.data))

        target_node, target_sum = dfs(root, 0, target)

        if not target_node:
            return -1

        return target_sum - leaf_sum(target_node, 0)
      
      
 """This is a solution to a problem where we are given a binary search tree (BST) and a target value, and we need to find the maximum difference between the target value and the sum of all leaf nodes in the BST.

The solution uses two recursive functions. The first one, dfs, performs a depth-first search of the BST to find the node with the target value, and calculates the sum of all the nodes visited during the search. The second function, leaf_sum, calculates the sum of all leaf nodes of a given subtree.

Finally, the solution subtracts the sum of leaf nodes from the path sum of the target node to obtain the maximum difference."""
