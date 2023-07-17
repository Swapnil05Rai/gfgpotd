class Solution:
    def FirstNonRepeating(self, A):
        a = [A[0]]
        b = a[0]
        c = a[0]

        for i in range(1, len(A)):
            if A[i] not in a:
                a.append(A[i])
                c += A[i]
            else:
                c = c.replace(A[i], '', 1)
            if c == '':
                b += "#"
            else:
                b += c[0]
        
        return b
