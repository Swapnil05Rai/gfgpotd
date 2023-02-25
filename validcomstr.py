class Solution:
    def checkCompressed(self,s, t):
        n, m = len(s), len(t)
        i, j = 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            elif t[j].isdigit():
                increment = 0
                while j < m and t[j].isdigit():
                    increment = increment * 10 + int(t[j])
                    j += 1
                i += increment
            else:
                return 0
        
        if i == n and j == m:
            return 1
        else:
            return 0
          
          
 """This is a Python function that checks if a string t is a compressed version of string s. The function returns 1 if t is a compressed version of s and 0 otherwise.

The function checks each character of s and t and if the characters match, it increments both i and j which are indices to the current character being compared in s and t respectively. If the characters don't match, the function checks if the current character in t is a digit. If it is a digit, the function parses the number and increments i by that amount. Otherwise, it returns 0 as the strings don't match.

The function returns 1 if the loop ends and i has reached the end of s and j has reached the end of t. If not, the function returns 0."""
