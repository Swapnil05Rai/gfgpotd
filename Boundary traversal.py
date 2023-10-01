class Solution:
    def BoundaryTraversal(self,matrix, n, m):
        # code here
        if n==1:
            return matrix[n-1]
        elif m==1:
            x=[]
            for i in range(n):
                x.append(matrix[i][0])
            return x
        result1=matrix[0]
        for i in range(1,n-1):
            result1.append(matrix[i][m-1])
        result2=matrix[n-1][::-1]
        for j in range(n-2,0,-1):
            result2.append(matrix[j][0])
        return result1+result2
