class Solution:
    def carpetBox(self,A, B, C, D):
        if C > D:
            C, D = D, C
        if A > B:
            A, B = B, A
        ans = 0
        while A > C or B > D:
            if A > C and B > D:
                B = B // 2
                ans += 1
            if A > B:
                A, B = B, A
            elif A > C:
                A = A // 2
                ans += 1
            if A > B:
                A, B = B, A
            elif B > D:
                B = B // 2
                ans += 1
            if A > B:
                A, B = B, A
        return ans
    
"""This code first checks if C is greater than D and swaps them if that is the case, and also checks if A is greater than B and swaps them if that is the case. 
Then it checks if the carpet can fit in the box by checking if either A or B is greater than C or D.
If it can't fit, it checks if both A and B are greater than C and D, and if so, it halves B and increments the count. 
If not, it checks if A is greater than B and swaps them if that is the case, then checks if A is greater than C and if so,
it halves A and increments the count. If not, it checks if B is greater than D and if so, it halves B and increments the count. 
Finally, it checks if A is greater than B and swaps them if that is the case. The function returns the count of the number of times the carpet was folded."""
