import math
def choose(n,r):
        req=math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
        return req
class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        ans=choose(2*n,n)//(n+1)
        return ans%(10**9+7)
