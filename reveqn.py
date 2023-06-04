class Solution:
    def reverseEqn(self, s):
        res=''
        i=0
        n=len(s)-1
        while i<=n:
            c=''
            while i <=n and s[i] not in ["*",'-','+',"/"]:
                c+=s[i]
                i+=1
            if i<n:
                c=s[i]+c
                i+=1
            res=c+res
        return res
