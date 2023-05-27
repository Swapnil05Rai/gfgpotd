def countnodes(self,head):
        if head==None:
            return 0
        else:
            
            listofvalues=[]
            temp=head
            while temp!=None:
                listofvalues.append(temp.data)
                temp=temp.next
            return listofvalues
    def modify_the_list(self, head):
        # code here
        vals=self.countnodes(head)
        n=len(vals)
        
        temp=head
        for i in range(n//2):
            temp.data=vals[n-i-1]-vals[i]
            temp=temp.next
        if n%2==1:
            n-=1
            temp=temp.next
        for i in range(n//2):
            temp.data=vals[n//2-i-1]
            temp=temp.next
            
        return head
      
      
"""countnodes(self, head):

This method takes a head parameter, which represents the head node of a linked list.
It initializes an empty list listofvalues to store the values of the nodes.
It then traverses the linked list using a temporary variable temp. At each node, it appends the value (temp.data) to the listofvalues list and moves to the next node.
Once the traversal is complete, it returns the listofvalues, which contains all the values of the nodes in the linked list.
modify_the_list(self, head):

This method also takes a head parameter representing the head node of a linked list.
It first calls the countnodes method to obtain the values of the nodes in the linked list.
It calculates the length of the vals list, which is the number of nodes in the linked list.
It initializes a temporary variable temp with the value of head.
Next, it performs modifications on the nodes of the linked list:
For the first half of the nodes (if the number of nodes is even), it assigns the difference between the value at the corresponding index from the end (vals[n-i-1]) and the value at the current index (vals[i]) to the data attribute of each node. It then moves temp to the next node.
If the number of nodes is odd, it skips the middle node by decrementing n and moving temp to the next node.
For the second half of the nodes, it assigns the value at the corresponding index from the beginning (vals[n//2-i-1]) to the data attribute of each node. It then moves temp to the next node.
Finally, it returns the modified head node.
In summary, the countnodes method calculates the values of the nodes in the linked list and returns them in a list. The modify_the_list method modifies the nodes of the linked list based on the values obtained from the countnodes method. The modifications involve assigning the difference between corresponding values from the end and the beginning of the list to the nodes in the first half (if the number of nodes is even) and assigning the values from the beginning to the nodes in the second half. The modified linked list is then returned."""
