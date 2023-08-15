def maxOnes(self, a, n):
        cnt = 0
        ans = 0
        for e in a:
            if e == 0:
                cnt += 1
            else:
                cnt -= 1
            cnt = max(0, cnt)
            ans = max(ans, cnt)
        return sum(a)+ans
 

