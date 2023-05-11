import math
class Solution:
    def minimumSum(self, s : str) -> int:
        
        i , j = 0 , len(s)-1
        
        stack = []
        
        c     = 0
        
        while i < j:
                
            if s[i] == s[j] and s[i]!="?":
                
                if stack:
                    
                    c+=2*(abs(ord(stack[-1])-ord(s[i])))
                    
            elif s[i] != s[j] and s[i]!="?" and s[j]!="?":
                
                return -1
                
            elif s[i] != s[j]:
                
                if s[i]!="?":
                    
                    if stack:
                        
                        c+=2*(abs(ord(stack[-1])-ord(s[i])))
                        
                else:
                    
                    if stack:
                        
                        c+=2*(abs(ord(stack[-1])-ord(s[j])))
                        
            if s[i] !="?":
                
                stack.append(s[i])
                
            elif s[j]!="?":
                
                stack.append(s[j])
                        
            i+=1
            j-=1
                 
        return c       
      
"""This code is implementing a solution to a problem where we are given a string s containing lowercase English letters and/or question marks (?). We need to replace all question marks with lowercase English letters such that the sum of absolute differences between the ASCII codes of the adjacent characters in the resulting string is minimized.

The main steps of the algorithm are as follows:

We initialize two pointers i and j to the first and last characters of the string s, respectively.
We initialize an empty stack stack and a variable c to keep track of the minimum sum of absolute differences.
We loop until i is less than j:
If s[i] and s[j] are equal and not equal to ?, we check if there are any characters in the stack. If there are, we pop the top element of the stack and add twice the absolute difference between its ASCII code and the ASCII code of the current character to c.
If s[i] and s[j] are not equal and not equal to ?, we return -1 as there is no way to replace the question marks to satisfy the given condition.
If s[i] and s[j] are not equal, we check if either of them is a question mark. If s[i] is not a question mark, we check if there are any characters in the stack. If there are, we pop the top element of the stack and add twice the absolute difference between its ASCII code and the ASCII code of s[i] to c. If s[i] is a question mark and s[j] is not a question mark, we check if there are any characters in the stack. If there are, we pop the top element of the stack and add twice the absolute difference between its ASCII code and the ASCII code of s[j] to c.
If s[i] is not a question mark, we push it onto the stack. If s[j] is not a question mark, we push it onto the stack.
We increment i and decrement j.
We return the minimum sum c.
Overall, this algorithm has a time complexity of O(n), where n is the length of the string s, since we are looping through each character of the string only once."""
