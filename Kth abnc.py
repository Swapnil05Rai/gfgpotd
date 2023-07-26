#User function Template for python3

def kthAncestor(root,k, node):
    #code here
    q = []
    found = False
    
    def inorder_traversal(root):
        nonlocal q, node, found
        
        if found or root is None:
            return 
        
        q.append(root)
            
        if root.data == node:
            found = True
            return 

        inorder_traversal(root.left)
        inorder_traversal(root.right)
        
        if not found:
            q.pop()
            
        
    inorder_traversal(root)
    if len(q)<=k:
        return -1
    return q[-k-1].data
