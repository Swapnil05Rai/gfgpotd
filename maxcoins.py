    def maxCoins(self, n, ranges):
        
        ranges.sort(key=lambda e: (e[1], e[0]))
        
        maxv, ends = [], []
        sofar, ans = 0, 0
        for start, end, v0 in ranges:
            lo, hi = 0, len(ends)
            while lo < hi:
                mi = lo+(hi-lo)//2
                if ends[mi] <= start:
                    lo = mi+1
                else:
                    hi = mi
            v = v0
            if 0 <= lo-1 < len(ends):
                v += maxv[lo-1]
            ans = max(ans, v)
            ends.append(end)
            sofar = max(sofar, v0)
            maxv.append(sofar)
        return ans
      
      
"""This function takes in an integer n and a list of tuples ranges. Each tuple in ranges represents a range [start, end] and a value v0. The goal is to maximize the sum of values v0 over non-overlapping ranges of [start, end] that cover the range [1, n].

The function first sorts the ranges based on the end points, and then uses binary search to find the largest index lo such that ends[lo] <= start (where ends is a list of end points of the already seen ranges). It then computes the value of the current range as v = v0 + maxv[lo-1], where maxv[lo-1] is the maximum value of all ranges whose end point is less than or equal to the start of the current range. The maximum sum of non-overlapping ranges is computed by keeping track of the maximum value seen so far sofar, and appending it to the maxv list for later use. The final answer is the maximum value seen throughout the iteration.

The function returns the maximum sum of values v0 over non-overlapping ranges of [start, end] that cover the range [1, n]."""
