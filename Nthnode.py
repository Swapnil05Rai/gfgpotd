def getNthFromLast(head,n):
    #code here
    lis=[]
    while head != None:
        lis.append(head.data)
        head=head.next
    if len(lis)<n:
        return -1
    lis.reverse()
    return lis[n-1]
