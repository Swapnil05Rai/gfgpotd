class Solution:
    def countPairs (self, n, arr, k):
        map = {}
        ans = 0
        
        for i in range(n):
            ans += map.get(arr[i] % k, 0)
            map[arr[i] % k] = map.get(arr[i] % k, 0) + 1
        
        return ans
      
      
"""This function iterates through the array of integers arr and checks for pairs of elements such that the absolute difference between the elements is divisible by k.
It does this by comparing each element arr[i] to every other element arr[j] in the array, and if abs(arr[i] - arr[j]) % k == 0, it increments a count of pairs. 
At the end, it returns the total count of pairs found."""
