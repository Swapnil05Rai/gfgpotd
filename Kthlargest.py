class Solution:
    def inOrder(self,root,ans):
        if not root:
            return 
        self.inOrder(root.left,ans)
        ans.append(root.data)
        self.inOrder(root.right,ans)
        
    def kthLargest(self,root, k):
        ans=[]
        self.inOrder(root,ans)
        ans.reverse()
        return ans[k-1]
