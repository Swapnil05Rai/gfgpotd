class Solution:
    def update(self, a, n, updates, k):
        # Your code goes here
        for x in updates:
            a[x-1]+=1
        for x in range(1,n):
            a[x]+=a[x-1]
