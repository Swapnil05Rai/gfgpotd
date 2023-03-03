class Solution:
    def minimumSquares(self, L,B):
        from math import gcd
        ans = gcd(L, B)
        count = (L // ans) * (B // ans)
        return [count, ans]

"""The function minimumSquares takes two arguments L and B, which are both of type long long int, and returns a vector of two long long int values: the first value represents the minimum number of identical squares that can be cut, and the second value represents the size of the squares.

The function first calculates the greatest common divisor (__gcd) of L and B and stores it in the variable ans. The number of squares that can be cut is then calculated by dividing the length and breadth of the rectangle by ans, and multiplying the results. The count and the size of the squares are returned as a vector of two values."""
