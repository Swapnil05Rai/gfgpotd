class Solution:
    def romanToDecimal(self, S):
        chrval={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val=0
        idx=0
        while idx<len(S)-1:
            if chrval[S[idx]]<chrval[S[idx+1]]:
                val-=chrval[S[idx]]
            else:
                val+=chrval[S[idx]]
            idx+=1
        return val+chrval[S[-1]]
