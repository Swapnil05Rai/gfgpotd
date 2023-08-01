 ans=[]
        vis=[0]*(V)
        def dfs(i):
            ans.append(i)
            vis[i]=1
            for i in adj[i]:
                if(vis[i]==0):
                    dfs(i)
        for i in range(V):
            if(vis[i]==0):
                dfs(i)
        return ans
