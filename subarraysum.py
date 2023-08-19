class Solution:
    def subArraySum(self,arr, n, s): 
        left, right = 0 , 0
        totalSum = 0
        while right < n  :
            totalSum += arr[right]
            while totalSum > s and left < right:
                totalSum -= arr[left]
                left += 1
            
            if totalSum == s:
                return [left + 1, right + 1]
            right += 1
                
        return [-1]
