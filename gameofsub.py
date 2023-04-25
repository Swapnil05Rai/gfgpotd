from typing import List

class Solution:
    def __init__(self):
        self.mod = int(1e9 + 7)
        self.mp = [0] * 31
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(2, 31):
            if i % 4 == 0 or i % 9 == 0 or i == 25:
                continue
            mask = 0
            for j in range(10):
                if i % primes[j] == 0:
                    mask |= 1 << j
            self.mp[i] = mask
    
    def pow(self, n: int) -> int:
        ans, m = 1, 2
        while n != 0:
            if n & 1 == 1:
                ans = (ans * m) % self.mod
            m = (m * m) % self.mod
            n >>= 1
        return ans
    
    def goodSubsets(self, n: int, arr: List[int]) -> int:
        one = 0
        dp = [0] * 1024
        cnt = [0] * 31
        dp[0] = 1
        for i in arr:
            if i == 1:
                one += 1
            elif self.mp[i] != 0:
                cnt[i] += 1
        
        for i in range(31):
            if cnt[i] == 0:
                continue
            for j in range(1024):
                if j & self.mp[i] != 0:
                    continue
                dp[j | self.mp[i]] = (dp[j | self.mp[i]] + dp[j] * cnt[i]) % self.mod
        
        ans = sum(dp) % self.mod - 1
        if one != 0:
            ans = (ans * self.pow(one)) % self.mod
        
        return ans


"""The given code implements a solution to the problem of finding the number of good subsets from an array of integers. A good subset is defined as a subset of array elements where no two elements share a common factor greater than 1.

The solution uses dynamic programming to solve the problem. First, it initializes a bitmask array "mp" which stores a binary mask for each integer from 2 to 30. The binary mask indicates which prime factors divide the integer. For example, the integer 6 has a binary mask of 101 (5th and 1st bit are set) since it is divisible by 2 and 3. The mask is used later to check if two numbers have any common prime factors.

Next, the function computes the power function which is used later for the final result. The power function is used to compute 2^n where n is the number of 1's in the array. The power function is implemented using bit manipulation.

The function then proceeds to count the number of 1's in the array and the number of elements that have a non-zero mask. It uses this information to initialize the dp array with 1 at position 0 (an empty subset). It then iterates through each element with a non-zero mask and for each, it iterates through each element in the dp array and checks if the binary OR of the mask with the current dp array element is zero. If it is, it updates the dp array at that position with the sum of its current value and the product of the count of the element and the value of the dp array at the previous position. This calculation counts the number of subsets that contain the current element with no common factors greater than 1.

Finally, the function sums all the values in the dp array, subtracts 1 to remove the empty subset, and multiplies it with 2^n where n is the number of 1's in the array. If there are no 1's in the array, the power function returns 1, which represents the empty subset. The final result is the number of good subsets modulo 10^9 + 7.

Overall, the solution runs in O(1024*n) time since it has to compute the number of good subsets for each possible subset of the binary mask. This is feasible since 1024 is a relatively small number.




"""
