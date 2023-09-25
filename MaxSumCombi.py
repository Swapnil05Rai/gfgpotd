import heapq
class Solution:
    def maxCombinations(self, n, k, a, b):
        a.sort()
        b.sort()
        ans=[]
        hp=[]
        for i in range(n):
            heapq.heappush(hp,[-(a[i]+b[-1]),i,n-1])
        
        while k:
            el,i,j=heapq.heappop(hp)
            ans.append(-el)
            heapq.heappush(hp,[-(a[i]+b[j-1]),i,j-1])
            k-=1
        return ans

