class Solution:
    def reverse(self, head: ListNode, k: int) -> ListNode:
        cur = head
        prev = None
        next_node = None
        count = 0
        while cur and count < k:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            count += 1
            
        if next_node is None:
            return prev
        
        head.next = self.reverse(next_node, float("inf"))
        return prev

      
   
 """The given code implements a recursive function to reverse every k nodes in a linked list.

The function takes two arguments - head, a pointer to the head of the linked list, and k, an integer denoting the number of nodes to be reversed at a time.

It initializes three pointers cur, prev, and next to head, NULL, and NULL respectively, and an integer c to 0.

It then runs a while loop until cur is not NULL and c is less than k. In each iteration, it stores the next pointer of cur, assigns prev to the next pointer of cur, and assigns cur to next. Finally, it increments c.

After the loop, if next is NULL, it returns prev, which is the new head of the reversed sub-list.

Otherwise, it recursively calls the reverse function with next as the head and INT_MAX as k (to reverse the remaining nodes). It then assigns the returned value to head->next.

Finally, it returns prev, which is the new head of the reversed sub-list."""
