def leastPrimeFactor (self, n):
        # code here 
        primes = [True]*(n+1)
        primes[0] = False
        primes[1] = False
        
        for i in range(2, n+1):
            if not primes[i]:
                continue
            for j in range(i*i, n+1, i):
                primes[j] = False
        primes = [i for i, e in enumerate(primes) if e]
        
        ans = [0]*(n+1)
        ans[1] = 1
        for i in range(2, n+1):
            for p in primes:
                if i%p == 0:
                    ans[i] = p
                    break
        return ans
