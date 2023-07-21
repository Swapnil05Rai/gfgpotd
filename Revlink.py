class Solution:
    def reverse(self,head, k):
        # Code here
        if head is None:
            return None
        curr=head
        prev=None
        i=0
        while curr and i<=(k-1):
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t
            i+=1
        p=self.reverse(curr,k)
        head.next=p
        return prev
