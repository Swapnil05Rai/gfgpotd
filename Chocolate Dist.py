class Solution:

    def findMinDiff(self, arr,n,m):
        arr.sort()
        min_diff = arr[n-1] - arr[0]
        for i in range(len(arr) - m + 1):
            min_diff = min(min_diff ,  arr[i + m - 1] - arr[i])
        return min_diff
