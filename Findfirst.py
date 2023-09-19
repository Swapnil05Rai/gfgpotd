  def getFirstSetBit(self,n):
        ans=1
        if n==0:
            return 0
        while n>0:
            res = n & 1
            if res==1:
                return ans
            ans+=1
            n = n>>1
        return 0
