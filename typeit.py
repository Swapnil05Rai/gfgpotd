class Solution:
    def minOperation(self, s): 
        #code here
        big = ''
        s1=''
        for x in range(len(s)):
            s1+=s[x]
            if s1 in s[x+1:]:
                big = s1
        if big:return len(s)-len(big)+1
        return len(s)
   
"""The method takes in a string as an input (s) and initializes two variables "big" and "s1" as empty strings.

It then loops through the characters in the input string (s) and adds them one by one to the variable "s1".

At each iteration, it checks if the current value of s1 can be found in the remaining part of the string s[x+1:].
If it is found, it means that s1 is a substring that is repeated in s, and the method assigns s1 to the variable "big".

After the loop, the method checks if the variable "big" has a value.
If it does, it returns the length of the input string s minus the length of the biggest repeated substring plus 1. 
If "big" is empty, it means that there is no repeated substring in s, and the method returns the length of the input string s.

The purpose of this code is to find the minimum number of operations needed to make the string non-repeating.
The code is finding the biggest repeated substring and returning the length of the string minus the length of the biggest repeated substring plus 1."""
