class Solution:
    
    #Function to find a solved Sudoku.
    def recur(self,i,empties):
        global rows,cols,ninecube,onetonine,flag,mat
        if i==len(empties):
            flag=True
            return
        
        li=empties[i]
        r=li[0]
        c=li[1]
        if r<=2:
            x=0
        elif r<=5:
            x=1
        else:
            x=2
        if c<=2:
            y=0
        elif c<=5:
            y=1
        else:
            y=2
        temp=list(set(onetonine)-(set(rows[r]).union(set(cols[c])).union(set(ninecube[x][y]))))
        # print(temp)
        for val in temp:
            mat[r][c]=val
            rows[r].append(val)
            cols[c].append(val)
            ninecube[x][y].append(val)
            self.recur(i+1,empties)
            if flag==True:
                return
            mat[r][c]=0
            rows[r].pop(-1)
            cols[c].pop(-1)
            ninecube[x][y].pop(-1)
        
        
    def SolveSudoku(self,grid):
        global rows,cols,ninecube,onetonine,flag,mat
        flag=False
        onetonine=[1,2,3,4,5,6,7,8,9]
        rows=[]
        cols=[]
        for i in range(9):
            rows.append([])
            cols.append([])
        
        mat=grid[:]
        # ninecube=rows.copy()
        ninecube = [[[] for _ in range(3)] for _ in range(3)]
        empties=[]
        # print(grid)
        for i in range(9):
            for j in range(9):
                if grid[i][j]!=0:
                    rows[i].append(grid[i][j])
                    cols[j].append(grid[i][j])
                    if i<=2:
                        x=0
                    elif i<=5:
                        x=1
                    else:
                        x=2
                    if j<=2:
                        y=0
                    elif j<=5:
                        y=1
                    else:
                        y=2
                    ninecube[x][y].append(grid[i][j])
                else:
                    empties.append([i,j])
        # print(rows)
        # print(cols)
        # print(ninecube)
        self.recur(0,empties)
        # print(mat)
        return flag
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for x in mat:
            for val in x:
                print(val,end=" ")
