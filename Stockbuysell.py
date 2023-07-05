from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        # code here
        result = 0
        for i in range(1, n):
            difference = prices[i] - prices[i-1]
            if prices[i] > prices[i-1]:
                result += difference
        return result
