import math
import bisect
from collections import defaultdict

class Solution:
    def countFractions(self, n, num, den):
        # Your code here]
        l=[]
        for i in range(n):
            x=math.gcd(num[i],den[i])
            l.append([num[i]//x,den[i]//x])
        
        l.sort()
        m=defaultdict(list);ans=0
        for i in l:
            if i[1] in m:
                l1=bisect.bisect_left(m[i[1]],i[1]-i[0])
                r1=bisect.bisect_right(m[i[1]],i[1]-i[0])
                ans+=(r1-l1)
            m[i[1]].append(i[0])
        return ans
