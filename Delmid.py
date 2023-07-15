
class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        return s.pop(int(((sizeOfStack+1)/2))-1)
        

