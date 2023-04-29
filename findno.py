class Solution:
    def findNumber(self, N : int) -> int:
        soln, prod = 0, 5
        digit = 1
        while (N - prod > 0):
            N -= prod
            prod *= 5
            digit += 1
        for i in range(1, digit + 1):
            for j in range(1, 10, 2):
                temp = 5 ** (digit - i)
                if temp == 0:
                    soln = soln * 10 + (2 * N) - 1
                    break
                if N - temp > 0:
                    N -= temp
                else:
                    soln = soln * 10 + j
                    break
        return soln
      
"""
This code is for finding the nth number in the sequence 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 25, 27, 29, 31, 35, 37, 39, 41, 45, 47, 49, 51, 55, 57, 59, 61, 65, 67, 69, 71, 75, 77, 79, 81, 85, 87, 89, 91, 95, 97, 99, 101, 105, 107, 109, 111, 115, 117, 119, 121, 125, ........

The algorithm works as follows:

First, it initializes soln to 0 and prod to 5. It also initializes digit to 1.
It then enters a loop that subtracts prod from N until N becomes less than prod. In each iteration, it multiplies prod by 5 and increments digit by 1.
Once the loop completes, it enters another loop that iterates from 1 to digit, and then from 1 to 9 (odd numbers only). For each digit in the number, it computes the appropriate digit by checking whether N is greater than or equal to 5^(digit - i), where i is the current digit. If it is, it subtracts 5^(digit - i) from N and moves on to the next digit. If not, it adds j (the current odd number) to the solution and moves on to the next digit. If 5^(digit - i) is 0 (i.e., if this is the last digit), it computes the digit differently as 2*N-1.
Finally, it returns the solution.
In other words, this code is essentially implementing a base-5 numbering system to generate the numbers in the sequence, and then converting the result back to base-10 to return the final answer.

"""
