class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        n = list(range(1,N+1))
        it = 1
        while K != len(n) and K < len(n):
            if it % 2 == 0:
                s=n[:-(K)]
                n.clear()
                n.extend(s)
                it += 1
            else:
                s=n[K:]
                n.clear()
                n.extend(s)
                it += 1
        if it % 2 == 0 and  len(n) > 1 :
            return n[0]
        elif len(n) > 1:
            return (n[-1])
        else:
            return n[0]
