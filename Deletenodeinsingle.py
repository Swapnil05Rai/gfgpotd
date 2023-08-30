def delNode(head, k):
    # Code here
    c=1
    a=head
    ptr=head.next
    prev=head
    if(head.next==None and k==1):
        return(-1)
    elif(head.next.next==None):
        if(k==2):
            head.next=None
            return(head)
        elif(k==1):
            head=head.next
            return(head)
        else:return(-1)
    else:   
        while(head and c<k):
            prev=head
            ptr=ptr.next
            head=head.next
            c+=1
        if(c==k and k!=1):
            prev.next=head.next
        elif k==1:
            head=ptr
            a=head
        return(a)
