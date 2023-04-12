from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        from bisect import bisect

        arr = arr[:n//2] + sorted(arr[n//2:])
        ans = 0
        for i in range(n//2):
            i = bisect(arr, arr[i]//5, n//2, n)
            ans += i-n//2
        return ans
        
        
"""The dominantPairs method takes an integer n and a list of integers arr as input and returns the number of pairs (arr[i], arr[j]) such that i < j and arr[i] * 5 <= arr[j].

The implementation first sorts the first half of the list and the second half of the list separately. Then, for each element in the first half, it calculates the index of the first element in the second half that satisfies the condition arr[i] * 5 <= arr[j] using the bisect method from the bisect module. Finally, it returns the total number of such pairs."""
