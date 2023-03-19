def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
       
        left, right = [0]*N, [0]*N
        lc, rc = set(), set()
        for i in range(N):
            lc.add(A[i])
            left[i] = len(lc)
            rc.add(A[N-1-i])
            right[N-1-i] = len(rc)
        
        ans = []
        for i in range(N):
            lc = 0 if i-1 < 0 else left[i-1]
            rc = 0 if i+1 >= N else right[i+1]
            ans.append(lc-rc)
        return ans
      
      
"""This function takes an integer N and a list of integers A as input, and returns a list of integers as output. For each index i in the list A, the output list contains the difference between the number of distinct integers in the subarray A[0:i] and the subarray A[i+1:N].

To calculate the number of distinct integers in the subarray A[0:i] for each index i, this function uses two arrays, left and right. The left array stores the number of distinct integers in the subarray A[0:i] for each index i, and the right array stores the number of distinct integers in the subarray A[i+1:N] for each index i. These arrays are filled using two sets, lc and rc, which store the distinct integers in the left and right subarrays, respectively.

The function then iterates over each index i in the list A, and calculates the number of distinct integers in the left subarray A[0:i] and the right subarray A[i+1:N] using the left and right arrays. The difference between these two values is then appended to the ans list, which is returned at the end of the function."""
