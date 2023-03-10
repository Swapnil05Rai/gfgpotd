class Solution:
    def maxTripletProduct (self, arr,  n): 
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')
        
        for num in arr:
            if num <= min2:
                if num <= min1:
                    min2 = min1
                    min1 = num
                else:
                    min2 = num
            if num >= max3:
                if num >= max2:
                    if num >= max1:
                        max2, max3 = max1, max2
                        max1 = num
                    else:
                        max3 = max2
                        max2 = num
                else:
                    max3 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)

"""To find the maximum triplet product

Find the maximum three numbers in the array, and get their product. The bigger the numbers, the bigger their product. It is possible that the array only consists of negative numbers, in that case too the maximum product possible would be the product of the maximum numbers.
Find the minimum two numbers in the array. If the array has more than 1 negative numbers, then these two minimum numbers would be negative. We find the product of the two negative numbers, which is always positive, and multiply it with the maximum number in the array.
In the second step, it is possible that the array does not have
any negative numbers, which would not give the maximum product, or
only one negative number, which would give us a negative number.
Hence, we compare the products from step 1, and step 2 to find the bigger number and return it."""
