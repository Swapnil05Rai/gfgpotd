from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        vis=[0]*(V)
        cou=[0]*(V)
        for i in adj:
            for j in i:
                cou[j]+=1
        q=deque()
        for i in range(V):
            if(cou[i]==0):
                q.append(i)
        ans=[]
        while(len(q)!=0):
            cur=q.popleft()
            ans.append(cur)
            for j in adj[cur]:
                cou[j]-=1
                if(cou[j]==0):
                    q.append(j)
        return ans
