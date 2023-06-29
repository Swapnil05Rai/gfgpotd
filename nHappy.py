def nextHappy (self, N):
        def happ(n):
            if n==1 or n==7 or n==10: 
                return True
            if n<10:
                return False
            s=0
            while n>0:
                s+=(n%10)**2
                n=n//10
            if happ(s): 
                return True
            return False
        N+=1
        while N!=10**5:
            if happ(N):
                return N
            else:
                N+=1
        return -1
