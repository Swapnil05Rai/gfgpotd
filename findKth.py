class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        fact = 1
        nums = []
        
        for i in range(1, n):
            fact *= i
            nums.append(i)
        nums.append(n)
        
        strr = ""
        k -= 1
        while True:
            strr += str(nums[k//fact])
            nums.pop(k//fact)
            if not nums:
                break
            k %= fact
            fact //= len(nums)
        return strr
