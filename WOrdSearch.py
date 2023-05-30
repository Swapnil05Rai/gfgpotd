class Solution:
	def isWordExist(self, board, word):
    	def help(b,w,i,j,l):
           if l==len(w):
                return True
           if i<0 or j<0 or i>=len(b) or j>=len(b[0]):
                return False
           if b[i][j]!=w[l]:
               return False
           b[i][j]="*"
           return (help(b,w,i-1,j,l+1) or 
           help(b,w,i+1,j,l+1)
           or help(b,w,i,j-1,l+1) 
           or help(b,w,i,j+1,l+1)
           )     
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and help(board,word,i,j,0):
                    return True
                   
        return False 
