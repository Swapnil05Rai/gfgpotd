from math import floor, log2

class Solution:
    def noConseBits(self, n: int) -> int:
        if n == 0:
            return n

        l = floor(log2(n))

        mask = (1 << l)
        cnt = 0
        while mask > 0:
            if mask & n != 0:
                cnt += 1
            else:
                cnt = 0

            if cnt == 3:
                n = n & (~mask)
                cnt = 0
            mask >>= 1
        return n

 """This function takes an integer n and returns an integer which is the same as n, except that it has no three consecutive 1 bits in its binary representation.

The function starts by computing the floor of the base-2 logarithm of n (i.e., the position of the most significant bit). It then creates a bit mask with a 1 in that position and zeroes elsewhere.

The function then iterates over the bits of n from left to right. For each bit, it checks whether it is a 1 or a 0, and updates a counter accordingly. If the counter reaches 3, it means that there are three consecutive 1 bits, so the current bit is set to 0 and the counter is reset to 0.

Finally, the function returns the modified value of n."""
