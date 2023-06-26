def nCr(self, n, r):
        mod = 10**9+7
        ans = 1
        for i in range(r):
            ans*=(n-i)
            ans//=(i+1)
            
        return ans%mod
