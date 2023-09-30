#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    row=[]
    col=[]
    for i in range(r):
      for j in range(c):
        if matrix[i][j]==1:
          row.append(i)
          col.append(j)
    row=set(row)
    row=list(row)
    col=set(col)
    col=list(col)
    a=0
    while a<len(row):
      for i in range(c):
        matrix[row[a]][i]=1
      a+=1 
    a=0
    while a<len(col):
      for i in range(r):
        matrix[i][col[a]]=1
      a+=1 
    return matrix
