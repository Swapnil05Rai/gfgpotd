class Solution:
    def singleNumber(self, nums):
        nums=sorted(nums)
        lst=[]
        for i in nums:
            if i in lst:
                lst.remove(i)
            else:
                lst.append(i)
        return lst
