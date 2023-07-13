from typing import List


class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        # code here
        from collections import Counter
        dic=Counter(arr)
        v=dic.values()
        l1=len(v)
        l2=len(set(v))
        return l1==l2
