class Solution:
    def findMinOpeartion(self, matrix, n):
        maxi=float('-inf')
        total=0
        for i in range(n):
            coli=0
            roi=0
            for j in range(n):
                total+=matrix[i][j]
                coli+=matrix[i][j]
                roi+=matrix[j][i]
                maxi=max(maxi,roi,coli)
        return maxi*n-total
                
