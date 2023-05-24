from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        # code here
        total = sum(arr)
       
        for i in range(N, 0, -1):
            if total % i == 0:
                return i
        
        return 0
        
