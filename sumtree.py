class Solution:
    def toSumTree(self, root):
        self.solve(root)

    def solve(self, r):
        if r is None:
            return 0
        oldv = r.data
        r.data = self.solve(r.left) + self.solve(r.right)
        return oldv + r.data
      
      
      
  """This code defines a Solution class with a method toSumTree() that takes a binary tree as input. The method toSumTree() calls another method solve() to convert the binary tree into a "sum tree".

A sum tree is a binary tree in which the value of each non-leaf node is equal to the sum of the values of its children. In this implementation, the solve() method is used to recursively convert the binary tree into a sum tree.

The solve() method takes a node r as input. If r is None, it returns 0. If r is not None, it stores the old value of the node's data in the variable oldv. It then sets the node's data to be the sum of the data of its left and right children, which are computed by recursively calling the solve() method on the left and right children of the node. Finally, the solve() method returns the old value plus the new value of the node's data.

In this way, the solve() method traverses the binary tree in a pre-order fashion and updates the value of each non-leaf node to be the sum of the values of its children, thus converting the binary tree into a sum tree.



"""
