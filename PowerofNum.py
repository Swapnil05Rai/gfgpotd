class Solution:    
    def modfun(self,N,R):
        if N==0:
            return 0
        if R==0:
            return 1 
        y=0
        if R%2==0:
            y=self.modfun(N,R/2) 
            y = (y * y) % 1000000007

        else:
                y = N % 1000000007 
                y = (y * self.modfun(N, R - 1) % 1000000007) % 1000000007
        return ((y + 1000000007) % 1000000007)
    
    
    def power(self,N,R):
        return self.modfun(N,R)
