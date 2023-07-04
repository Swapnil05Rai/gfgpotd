class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        count =0 
        product=1
        j=0
        for i in range(n):
            product*=a[i]
            while(product>=k and j<=i):
                product /= a[j]
                j+=1
            count += (i-j+1);
        return count
