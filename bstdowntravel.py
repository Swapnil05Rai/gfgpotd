class Solution:
    def findTarget(self, root, target):
        if root is None:
            return None
        if root.data == target:
            return root
        if root.data > target:
            return self.findTarget(root.left, target)
        return self.findTarget(root.right, target)
        
    def traverseVertically(self, root, position):
        if root is None:
            return 0
        left = self.traverseVertically(root.left, position + 1)
        right = self.traverseVertically(root.right, position - 1)
        return (root.data if position == 0 else 0) + left + right
    
    def verticallyDownBST(self, root, target):
        result = self.findTarget(root, target)
        if result is None:
            return -1
        return self.traverseVertically(result, 0) - result.data

      
"""The solution has three functions:

findTarget: This function takes a binary search tree root and a target target as input, and returns the node in the BST that has the value equal to the target.
It does this by traversing the BST and comparing the value of each node with the target. If the value of a node is equal to the target, it returns that node. 
If the value of a node is greater than the target, it goes to the left child of the node.
If the value of a node is less than the target, it goes to the right child of the node.

traverseVertically: This function takes a binary search tree root and a position position as input,
and returns the sum of all the nodes that are vertically below the current node at a given position. 
The function does this by using a recursive approach.
First, it calls the traverseVertically function on the left child of the current node and adds the returned value to the current sum.
Then, it calls the traverseVertically function on the right child of the current node and adds the returned value to the current sum. 
Finally, if the current node is at the target position (i.e., position is equal to 0), it adds the value of the current node to the sum.

verticallyDownBST: This function takes a binary search tree root and a target target as input,
and returns the sum of all the nodes vertically below the node with the value equal to the target. 
It does this by first calling the findTarget function to get the node with the value equal to the target. 
If the node is found, it calls the traverseVertically function on that node with a starting position of 0,
and returns the sum minus the value of the target node. If the target node is not found, it returns -1.

In essence, this solution finds the target node in the BST using the findTarget function and calculates the sum of all the nodes vertically below the target node using the traverseVertically function.



"""
