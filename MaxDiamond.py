from sortedcontainers import SortedList

class Solution:
    def maxDiamonds(self, A, N, K):
        A = SortedList(A)
        Tsum = 0
        
        while(K):
            x = A.pop()
            Tsum += x
            A.add(x // 2)
            K -= 1
            
        return Tsum
