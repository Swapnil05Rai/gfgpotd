class Solution:
    def solve(self, arr, target, index, dp):
        # Base case
        if index==0:
            return arr[0]==target
        if dp[index][target]!=-1:
            return dp[index][target] 
        pick=0
        if target>=arr[index]:
            pick = self.solve(arr, target-arr[index], index-1, dp)
        notpick = self.solve(arr, target, index-1, dp)
        dp[index][target] = pick or notpick
        return dp[index][target]
    
    def equalPartition(self, N, arr):
        summ=sum(arr)
        if summ%2 != 0:
            return 0
        target = summ//2
        dp = [[-1 for i in range(target+1)] for j in range(len(arr)+1)]
        
        return self.solve(arr, target, len(arr)-1, dp)
