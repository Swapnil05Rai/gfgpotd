from typing import List

class Solution:
    def findMaxSubsetSum(self, N : int, a : List[int]) -> int:
        take=n_take=0
        for i in a:
            take,n_take=max(i+take,n_take),i+take
        return max(take,n_take)
