from itertools import permutations
class Solution:
    def find_permutation(self, S):
        s=permutations(S)
        li=["".join(i)for i in s]
        lis=list(set(li))
        lis.sort()
        return lis
