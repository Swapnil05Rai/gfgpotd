class Solution:
    def transpose(self, matrix, n):
    
        for i in range(0,n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
