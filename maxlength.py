
class Solution():
    def solve(self, a, b, c):
        p = [a,b,c]
        p.sort()
        z = p[-1]
        if z - 3 >= 2 * (p[0]+p[1]):
            return -1
        else:
            return a+b+c
          
"""The solve function takes three integer parameters a, b, and c. 
It first puts these three numbers into a list p and sorts them. It then assigns the largest number in p to the variable z. 
If the difference between z and 3 is greater than or equal to two times the sum of the other two numbers in p, the function returns -1.
Otherwise, it returns the sum of a, b, and c.
In other words, the function checks if the largest number is too far away from the other two numbers and, 
if so, returns -1, otherwise, it returns the sum of the three numbers."""
