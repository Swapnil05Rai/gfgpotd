def removeDuplicates(head):
    if head==None:
        return head
    curr=head
    while curr.next is not None:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head
