class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        total = n*m
        sr,sc,er,ec = 0,0,n-1,m-1
        while sc<=ec and sr<=er:
            for i in range(sc,ec+1):
                k-=1
                if k==0:
                    return a[sr][i]
            sr+=1
            for i in range(sr,er+1):
                k-=1
                if k==0:
                    return a[i][ec]
            ec-=1
            for i in range(ec,sc-1,-1):
                k-=1
                if k==0:
                    return a[er][i]
            er-=1
            for i in range(er,sr-1,-1):
                k-=1
                if k==0:
                    return a[i][sc]
            sc+=1
