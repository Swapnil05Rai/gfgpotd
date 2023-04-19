class Solution:
    def wifiRange(self, N, S, X): 
        j=-1
        for i in range(N):
            if S[i]=='1':
                if i-j-1>X:
                    return False
                j=i+X
        if j>=N-1:
            return True
        return False
      
"""This code implements a function wifiRange that takes in three arguments: N, S, and X, where N is an integer indicating the total number of points along a line, S is a string of 0s and 1s indicating the presence or absence of a wifi signal at each point, and X is an integer indicating the maximum distance a wifi signal can reach.

The function checks if it is possible to have a wifi signal at each point on the line by checking if the distance between two consecutive 1s is less than or equal to X. If the distance between two consecutive 1s is greater than X, it means that there is a gap where the wifi signal cannot reach, and hence the function returns False.

The function returns True if there is a wifi signal at the last point on the line, and False otherwise."""
