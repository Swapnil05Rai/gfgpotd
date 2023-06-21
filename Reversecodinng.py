class Solution:
    def sumOfNaturals(self, n):
        mod = 1e9 + 7
        tsum = (n * (n + 1)) // 2
        
        return int(tsum % mod)
