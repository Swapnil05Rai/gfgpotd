from typing import List

class Solution:

    def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:
        intervals.sort( key=lambda x: (x[1], x[0]) )
        M = intervals[-1][1]
        dp = [0]*(M+1)
        
        for i in range(n):
            s,e,p = intervals[i]
            if p+dp[s] > dp[e]:
                dp[e] = p+dp[s]
            if i < n-1:
                _,en,_ = intervals[i+1]
                for j in range(e+1, en+1):
                    dp[j] = dp[e]
                
        return dp[M]
      
      
"""The idea behind this approach is that if we sort the intervals based on their ending points, we can process them in a way that ensures that we only consider non-overlapping intervals. This is because if we have two intervals [s1, e1, p1] and [s2, e2, p2] where e1 <= s2, then if we sort the intervals based on their ending points, the interval with the smaller ending point (e1) will be processed before the interval with the larger ending point (e2).

The code then uses a dynamic programming approach to find the maximum profit achievable. It maintains a dp array where dp[i] represents the maximum profit achievable from the intervals ending at i. For each interval, it checks if the profit from including the interval is greater than the profit from not including it. If it is, it updates the dp value for the ending point of the interval.

The time complexity of this solution is O(n^2) as we are sorting the intervals and for each interval, we are iterating through the previous intervals. The space complexity is O(n) as we are using a dp array of size n."""
