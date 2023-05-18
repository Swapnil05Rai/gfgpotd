class Solution:
	def closedIslands(self, matrix, N, M):
	    delr=[-1,0,1,0]
	    delc=[0,1,0,-1]
	    def dfs(i,j):
	        matrix[i][j]=-1
	        for _ in range(4):
	            newr=i+delr[_]
	            newc=j+delc[_]
	            if newr>=0 and newr<N and newc>=0 and newc<M and matrix[newr][newc]==1:
	                dfs(newr,newc)
	        
		for i in range(M):
		    if matrix[0][i]==1:
		        dfs(0,i)
		    if matrix[N-1][i]==1:
		        dfs(N-1,i)
		for i in range(N):
		    if matrix[i][0]==1:
		        dfs(i,0)
		    if matrix[i][M-1]==1:
		        dfs(i,M-1)
		ans=0
    	for i in range(N):
    	    for j in range(M):
    	        if matrix[i][j]==1:
    	            dfs(i,j)
    	            ans+=1
		return ans
  
