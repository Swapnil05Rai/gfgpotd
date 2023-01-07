class Solution:
    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        result = None
        if a.data <= b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)

        return result

    def flatten(self, root):
        if root is None or root.next is None:
            return root
        return self.merge(root, self.flatten(root.next))

      
      
 """The flatten function is a recursive function that flattens a linked list of sub-linked-lists. It works by continuously merging sub-linked-lists together until it gets a single, sorted linked list.

The merge function is a helper function that takes in two sub-linked-lists and merges them together. It does this by comparing the data values of the head nodes of the two lists and adding the smaller one to the result list. It then recursively calls itself with the bottom pointers of the two lists as input to merge the rest of the nodes.

The flatten function works by dividing the input linked list into two sub-linked-lists using the next pointers, and then recursively flattening each of the sub-linked-lists. It then merges the two flattened sub-linked-lists together using the merge function.

The base case for the recursion is when the input linked list has no more nodes (i.e., it is None) or has only one node (i.e., its next pointer is None). In these cases, the function simply returns the input linked list.

"""
