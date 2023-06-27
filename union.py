class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        li=[]
        p1=head1
        p2=head2
        while(head1):
            li.append(head1.data)
            head1=head1.next
        while(head2):
            li.append(head2.data)
            head2=head2.next
        li=list(set(li))
        li=sorted(li)
        j=Node(0)
        p=j
        for i in li:
            j.next=Node(i)
            j=j.next
        head1=p1
        head2=p2
        return p.next
