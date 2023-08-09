import math
class Solution:
    def largestPrimeFactor (self, N):
        # code here
        i = 2
        while(i<=int(math.sqrt(N))):
            if N%i == 0:
                N = N//i
                i-=1
            i+=1
        return N
