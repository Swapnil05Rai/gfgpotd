def reverseLLUsingStack(head):
    stack, temp = [], head
    while temp:
        stack.append(temp)
        temp = temp.next
    head = temp = stack.pop()
    while len(stack) > 0:
        temp.next = stack.pop()
        temp = temp.next
    temp.next = None
    return head
class Solution:
    def compute(self,head):
        head=reverseLLUsingStack(head)
        #return(head)
        ans=head
        maxi=head.data
        prev=head
        head=head.next
        while(head!=None):
            if head.data>=maxi:
                maxi=head.data
                prev.next=head
                prev=head
            head=head.next
        prev.next=None
        return(reverseLLUsingStack(ans))

