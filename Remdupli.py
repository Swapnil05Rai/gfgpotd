 def removeDuplicates(self, head):
        # code here
        # return head after editing list
        d={}
        curr=head
        prev=None
        while curr!=None:
            if curr.data in d:
                prev.next=curr.next
                curr=curr.next
            else:
                d[curr.data]=1
                prev=curr
                curr=curr.next
        return head
