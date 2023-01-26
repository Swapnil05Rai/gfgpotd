class Solution:
    def caseSort(self, S, N):
        lower = []
        upper = []
        for i in range(N):
            if S[i].isupper():
                upper.append(S[i])
            else:
                lower.append(S[i])
        upper.sort()
        lower.sort()
        i = 0
        j = 0
        result = list(S)
        for k in range(N):
            if result[k].isupper():
                result[k] = upper[i]
                i += 1
            else:
                result[k] = lower[j]
                j += 1
        return "".join(result)


"""This code defines a Solution class, which contains a method called caseSort. 
The caseSort method takes two arguments: a string S and an integer N, which is the length of the string.
The method separates the uppercase and lowercase characters of the given string S into two separate lists upper and lower. 
Then it sorts each list separately using the sort() method. 
Then it iterates through the original string, replacing each character with the next character from the appropriate sorted list, either the lowercase or uppercase list.
Finally it returns the sorted string.
It has Time complexity of O(Nlog(N)) and an auxiliary space of O(N)."""
