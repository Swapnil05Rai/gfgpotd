class Solution:
    def countSpecialNumbers(self, n, arr):
        m = max(arr)
        res = [0]*(m+1)
        for a in arr:
            if res[a] <= 1:
                for b in range(a, m+1, a):
                    res[b] += 1
        return sum(res[a] > 1 for a in arr)


"""This function countSpecialNumbers takes an integer n and a list arr of integers as input, and returns the number of integers in the list that have more than one factor in the range [1, max(arr)].

The function first determines the maximum value m in the list arr, and creates a list res of length m+1 filled with zeros. For each element a in the list arr, the function checks if the value in the res list at index a is less than or equal to 1. If it is, the function loops over all multiples of a in the range [a, m+1] and increments the corresponding value in the res list.

Finally, the function loops over all elements a in the list arr and counts the number of elements in the res list that have a value greater than 1. This count is returned as the result of the function."""
