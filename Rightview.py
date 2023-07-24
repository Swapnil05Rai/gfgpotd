from collections import deque
class Solution:
    # Function to return list containing elements of right view of binary tree.
    @staticmethod
    def rightView(root):
        if root is None:
            return []
     
        q = deque()
        q.append(root)
        right_view_list = []
     
        while q:
            # Get number of nodes for each level
            n = len(q)
     
            # Traverse all the nodes of the current level
            while n > 0:
                n -= 1
     
                # Get the front node in the queue
                node = q.popleft()
     
                # Add the last node of each level to the result list
                if n == 0:
                    right_view_list.append(node.data)
     
                # If left child is not null, push it into the queue
                if node.left:
                    q.append(node.left)
     
                # If right child is not null, push it into the queue
                if node.right:
                    q.append(node.right)

        return right_view_list
