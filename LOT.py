#User function Template for python3


#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here
    if root == None:
        return []
    q = [root]
    ans = []
    flag = 1
    while len(q) != 0:
        size = len(q)
        temp = []
        while size != 0:
            cur = q.pop(0)
            temp.append(cur.data)
            if cur.left != None:
                q.append(cur.left)
            if cur.right!=None:
                q.append(cur.right)
            size -= 1
        
        if flag % 2 != 0:
            temp = temp[::-1]
        for i in temp:
            ans.append(i)
        flag += 1
            
    return ans
