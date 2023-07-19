#User function Template for python3
class Solution:

    def longestPalinSubseq(self, S):
        a=S
        S=S[::-1]
        dp=[[0 for _ in range(len(S)+1)] for _ in range(len(S)+1)]
        for i in range(len(S)+1):
            for j in range(len(S)+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif S[i-1]==a[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
