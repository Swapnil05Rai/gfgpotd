def addMinChar (self, str1):
        s = str1 + "@" + str1[::-1]
        n = len(s)
        p = [0]*(n+1)
        p[0] = -1
        for i in range(1, n+1):
            k = p[i-1]
            while k > 0 and s[k] != s[i-1]:
                k = p[k]
            p[i] = k+1
        return len(str1) - p[n]
      
"""This function adds the minimum number of characters to the given string to make it a palindrome.
It does so by first creating a new string which is the concatenation of the given string, a separator character ('@' in this case),
and the reverse of the given string. Then, it computes the longest proper suffix of the new string that matches its prefix using the KMP algorithm.
The length of this suffix is the number of characters that need to be added to the original string to make it a palindrome."""
