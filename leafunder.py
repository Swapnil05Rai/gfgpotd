class Solution:
    def getCount(self,root,n):
        #code here
        map=[]
        que=deque()
        que.append(root)
        round=1
        while que:
            for _ in range(len(que)):
                cur=que.popleft()
                if not cur.left and not cur.right:
                    map.append((round,cur.data))
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            round+=1
        ans,i=0,0
        while i<len(map) and ans<=n:
            ans+=map[i][0]
            if ans<=n:
                i+=1
        return i
