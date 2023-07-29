def findMedian(root):
    l=[]
    inorder(root,l)
    n=len(l)
    if n%2==0:
        ans=l[(n//2)-1]+l[n//2]
        if ans%2==0:
            return ans//2
        else:
            return ans/2
    else:
        return l[n//2]
def inorder(root,ans):
    if root==None:
        return 
    inorder(root.left,ans)
    ans.append(root.data)
    inorder(root.right,ans)
