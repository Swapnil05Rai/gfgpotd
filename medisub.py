def countSubarray(self, N, A, M): 
        # code here
        def fn( n, A, m):
            mp = [0]*(2*n+1)
            cur,tot,ans = n, 0, 0
            mp[cur]+=1
            
            for i in range(n) :
                x = -1
                if (A[i] >= m) :
                    x = 1
                if (x == -1) :
                    tot -= mp[(cur+x)]
                else :
                    tot += mp[cur]
                
                cur += x
                ans += tot
                mp[cur]+=1
                
            return ans
        
        return fn(N, A, M) - fn(N, A, M+1)
  
"""The given code calculates the number of subarrays in an array whose sum is between M+1 and M. It uses a sliding window approach with a frequency array to keep track of the frequency of each subarray sum. The main function calls a helper function to perform this calculation and returns the difference between the results of two helper function calls with different values of M."""
