class Solution:
    def nthFibonacci(self, n : int) -> int:
        x1=1
        x2=1
        if(n==1):
            return 1
        elif(n==2):
            return 1
        while(n>2):
            x=0
            x=(x1+x2)%(1e9+7)
            x1=x2
            x2=x
            n-=1
        return int(x)
