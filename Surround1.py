def Count(self, matrix):
        ones=0
        # Code here
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                count=0
                if matrix[x][y]==1:
                    if y-1>=0 and matrix[x][y-1]==0:
                        count+=1
                    if y+1<len(matrix[0]) and matrix[x][y+1]==0:
                        count+=1
                    if x-1>=0:
                        if matrix[x-1][y]==0:
                            count+=1
                        if y-1>=0 and  matrix[x-1][y-1]==0:
                            count+=1
                        if y+1<len(matrix[0]) and matrix[x-1][y+1]==0:  
                            count+=1
                    if x+1<len(matrix):
                        if matrix[x+1][y]==0:
                            count+=1
                        if y-1>=0 and matrix[x+1][y-1]==0:
                            count+=1
                        if y+1<len(matrix[0]) and matrix[x+1][y+1]==0:
                            count+=1
                    if count%2==0 and count!=0:
                        ones+=1
        return ones  
