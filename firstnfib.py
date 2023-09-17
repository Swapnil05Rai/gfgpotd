class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        res = [1]*n
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res
