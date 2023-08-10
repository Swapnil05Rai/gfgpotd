class Solution:

    def lcs(self,x,y,s1,s2):
        dp=[[0]*(y+1) for z in range(x+1)]
        for i in range(x):
            for j in range(y):
                if s1[i]==s2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]
