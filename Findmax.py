from typing import List


class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        from itertools import accumulate
        As = [ set(accumulate(reversed(S))) for S in (S1, S2, S3) ]
        A = As[0] & As[1] & As[2]
        return max(A) if A else 0
