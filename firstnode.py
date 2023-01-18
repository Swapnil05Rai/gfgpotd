class Solution:
    def findFirstNode(self, head):
        # Initialize two pointers, one moving at a slower pace and the other moving at a faster pace
        tortoise = head
        hare = head

        # Iterate through the linked list until the hare pointer reaches the end or a loop is found
        while (hare != None and hare.next != None):
            tortoise = tortoise.next
            hare = hare.next.next
            if (tortoise == hare):
                break

        # If no loop is found, return -1
        if (hare == None or hare.next == None):
            return -1

        # Otherwise, set the tortoise pointer back to the head of the linked list
        tortoise = head

        # Iterate through the linked list again until the tortoise pointer meets the hare pointer
        while (tortoise != hare):
            tortoise = tortoise.next
            hare = hare.next

        # Return the value of the first node of the loop
        return tortoise.data
"""The "findFirstNode" function finds the first node of a loop in a singly linked list.
It uses the Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm. 
Two pointers, one moving at a slower pace and the other at a faster pace are used. 
If there is a loop in the linked list, the hare pointer will eventually catch up to the tortoise pointer.
At that point, the function will use the pointers to find the first node of the loop and return its data.
If no loop is found, the function will return -1. The time complexity of this algorithm is O(N) and the auxiliary space is O(1)."""
