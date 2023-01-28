from collections import Counter
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str):
        if Counter(s1) != Counter(s2):
            return False
        if len(s1) == 1:
            return True
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False

      
      
"""If strings are not anagrams, return False.
If length of string is 1, return True
 Otherwise, try parition the strings at different position to see if they are scramled. At each position there are two options. 
Check isScramble(prefix of S1, prefix of S2) and isScramble(suffix of S1, suffis of S2)
Check isScramble(prefix of S1, suffix of S2) and isScramble(suffix of S1, prefix of S2)
Memoize entire solution to avoid recomputing overlapping subproblems."""
