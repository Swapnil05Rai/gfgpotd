from collections import deque
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if A[0][0]==0 or A[X][Y]==0:
            return -1
        # dist=[[0 for i in range(M)] for i in range(N)]
        visited=[[False for i in range(M)] for i in range(N)]
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        q=[]
        q.append((0,0,0))
        def isvalid(r,c):
            return (r>=0 and r<N and c>=0 and c<M)
        
        while q:
            dist,row,col=q.pop(0)
            visited[row][col]=True
            if row==X and col==Y:
                return dist
            for i in range(4):
                r=row+delrow[i]
                c=col+delcol[i]
                if isvalid(r,c) and visited[r][c]==False and A[r][c]==1:
                    
                    visited[r][c]=1
                    q.append((dist+1,r,c))
        return -1
