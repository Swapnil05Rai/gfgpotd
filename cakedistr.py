class Solution:
  def maxSweetness(self, sweetness, n, k):
        def ok(minv):
            s, cnt = 0, 0
            for e in sweetness:
                s += e
                if s >= minv:
                    cnt += 1
                    s = 0
            return cnt >= k+1
            
        lo, hi = min(sweetness), sum(sweetness)+1

        while lo < hi:
            mi = lo+(hi-lo)//2
            if not ok(mi):
                hi = mi
            else:
                lo = mi+1
        return lo-1



"""This is a binary search algorithm to find the maximum sweetness value of a piece of chocolate that can be obtained by dividing a given array of sweetness values into k+1 non-empty subarrays.

The ok function checks if it is possible to divide the chocolate into k+1 non-empty subarrays, such that the sweetness value of each subarray is greater than or equal to minv.

The binary search is performed on the range of possible sweetness values of the pieces of chocolate, i.e., between the minimum sweetness value in the given array and the sum of all sweetness values. The loop continues until the lo and hi values converge.

In each iteration, the middle sweetness value mi is checked by the ok function. If ok returns False, this means that the current mi value is too high and needs to be decreased, so hi is set to mi. Otherwise, mi is too low and needs to be increased, so lo is set to mi+1.

Finally, the result is the maximum sweetness value that satisfies the condition, which is lo-1."""
