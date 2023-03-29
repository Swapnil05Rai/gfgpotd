class Solution:
    def countSubstring(self, s: str) -> int:
        m = {0: 1}
        cnt = 0
        ans = 0
        for c in s:
            cnt += 1 if c.isupper() else -1
            ans += m.get(cnt, 0)
            m[cnt] = m.get(cnt, 0) + 1
        return ans
      
"""This is a solution for the problem of counting the number of substrings of a given string s which have an equal number of uppercase and lowercase letters.

The solution uses a dictionary m to keep track of the number of times a certain difference cnt between the number of uppercase and lowercase letters has been seen in the string so far. The difference is incremented by 1 if a lowercase letter is encountered, and decremented by 1 if an uppercase letter is encountered.

For each character in the string, the solution calculates the current cnt and adds the number of times it has been seen so far to the answer. It also updates the value in the dictionary for cnt.

Finally, the solution returns the total number of substrings that have an equal number of uppercase and lowercase letters.





"""
