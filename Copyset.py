class Solution:
    def setSetBit(self, x, y, l, r):
        y = y & (2**r - 1)
        y = y & (-1<<(l-1))
        return y | x
