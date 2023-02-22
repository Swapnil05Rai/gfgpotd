from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque([root])
        
        while queue:
            sz = len(queue)
            for i in range(sz):
                curr = queue.popleft()
                if i == sz - 1:
                    curr.nextRight = None
                else:
                    curr.nextRight = queue[0]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return root

      
"""code uses the deque module to implement the queue data structure. It defines a function connect that takes a root node of type Node as input and returns the root node after connecting all the nodes on the same level to their right neighbors.

The function initializes a deque queue with the root node and iterates through the deque until it's empty. For each level, it first obtains the size of the deque, and then iterates through the deque sz number of times. It pops the leftmost node curr from the deque and checks if it's the last node in the level. If it's the last node, it sets its nextRight pointer to None, otherwise, it sets its nextRight pointer to the leftmost node of the next level. It also appends its left and right children to the deque if they exist.

Finally, the function returns the root node after all the nodes on the same level are connected to their right neighbors."""
