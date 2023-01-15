from collections import defaultdict
class Solution():
    def countSubstring(self, S):
        ac, le, car = 0, defaultdict(lambda:0), defaultdict(lambda:0)
        le[0] = 1; car[1] = 1
        ans = 0
        for c in S:
            v = 1 if c=='1' else -1
            ac += v
            le[ac] += 1 + car[ac]
            car[ac+1] += 1 + car[ac]
            car[ac] = 0
            ans += le[ac-1]
        return ans
 """This code is a solution for counting the number of substrings in a given string S that consist of an equal number of 0's and 1's.
 It uses a defaultdict to keep track of the number of substrings with a given count of 0's minus 1's,
 and another defaultdict to keep track of substrings that carry over to the next count. 
 The variable "acc" keeps track of the current count of 0's minus 1's, and the variable "ans" keeps track of the total number of substrings."""
