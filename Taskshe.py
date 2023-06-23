class Solution:
    def leastInterval(self, N, K, tasks):
        # Code here
        freq = {}
        
        for i in tasks:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
                
        
        max_freq = max(freq.values())
        
        ans = (K + 1) * (max_freq - 1)
        
        for i in freq.values():
            if max_freq == i:
                ans += 1
        
        return max(ans, N)
