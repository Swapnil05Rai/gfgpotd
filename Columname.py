class Solution:
    def colName (self, n):
        # your code here
        s=""
        while(n>0):
            n-=1
            p=(n)%26
            s+=chr(ord('A')+p)
            n=n//26
        return s[::-1]
            
