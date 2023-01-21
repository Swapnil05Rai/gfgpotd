class Solution:

    def minVal(self, a: int, b: int) -> int:
        count = 0
        for i in range(30):
            if b & (1<<i):
                count += 1
        val = 0
        for i in range(29, -1, -1):
            if count > 0:
                if a & (1 << i):
                    count -= 1
                    val += (1 << i)
            else:
                break
        for i in range(30):
            if count > 0:
                if not val & (1 << i):
                    count -= 1
                    val += (1 << i)
            else:
                break
        return val
      
"""This code finds the minimum value of X such that the number of set bits in X is equal to the number of set bits in B, and (X XOR A) is minimum possible.

First, it finds the count of set bits in B by iterating through all the bits of B and checking if they are set or not.

Then it iterates through the bits of A starting from the most significant bit (MSB) and going down to the least significant bit (LSB). For each bit, check if it is set in A and not set in B. If so, set the corresponding bit in X.

Then it again iterates through all the bits of X and if there are still some remaining count of set bits left and if that bit is not set in X then it sets that bit in X.

This way it constructs X such that the count of set bits in X is equal to the count of set bits in B and the XOR of X and A will be minimized."""
