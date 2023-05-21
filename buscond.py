class Solution:
    def findMoves(self,n,chairs,passengers):
        #code here
        chairs.sort()
        passengers.sort()
        count=0
        for i in range(n):
            count+=abs(passengers[i]-chairs[i])
        return count
