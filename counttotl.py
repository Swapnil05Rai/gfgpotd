import math
class Solution:
    def countBits(self, N : int) -> int:
        if(N <= 1):
            return N
        x = math.floor(math.log2(N));
        return x*(1<<(x-1)) + (N - (1<<x) + 1) + self.countBits(N - (1<<x));
