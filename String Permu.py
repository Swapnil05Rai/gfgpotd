from itertools import permutations

class Solution:
    def permutation(self,s):
        r = list(permutations(s))
        result = [''.join(i) for i in r]
        result.sort()
        return result
