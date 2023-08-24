class Solution:
    def multiplyStrings(self,s1,s2):
        def mul(s):
            prod=0
            for i in range(len(s)):
                if s[i]!='-':
                    prod=prod*10+(ord(s[i])-ord('0'))
            return prod
        m,n=len(s1),len(s2)
        st1=[]
        st2=[]
        for i in range(m):
            if s1[i]!=0:
                st1.append(s1[i])
        for i in range(n):
            if s2[i]!=0:
                st2.append(s2[i])
        x=-1*(mul(st2))if st2[0]=='-' else mul(st2)
        y=-1*(mul(st1))if st1[0]=='-' else mul(st1)
        return x*y
        
