import math
class Solution:
    def isLucky(self, n): 
        #RETURN True OR False
        i=2
        while i<=n:
            if n%i==0:
                return 0
            n-=n//i  
            i+=1
        return 1   
