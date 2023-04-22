def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        c = sorted((e, i) for i, e in enumerate(arr))
        sums = [0]*len(c)
        repeat = 1
        ans = [0]*n
        for i in range(1, n):
            if c[i][0] == c[i-1][0]:
                sums[i] = sums[i-1]
                repeat += 1
            else:
                sums[i] = sums[i-1]+c[i-1][0]*repeat
                repeat = 1
            ans[c[i][1]] = sums[i]
        
        return ans
      
"""This function takes an integer n and a list arr of length n. The list arr contains n integers. The function returns a list of length n, where the i-th element of the returned list is the sum of all elements in arr that are smaller than the i-th element.

The function first sorts the elements of the list arr along with their indices using the sorted function. The c variable will hold the sorted list along with their indices.

Then, the function initializes a list sums with all elements set to 0 and another variable repeat with value 1. The ans variable is also initialized as a list of length n, with all elements set to 0.

Then, for each element in the sorted list c, the function checks if the current element is equal to the previous element. If it is, it means that we have another occurrence of the same value in the list. In this case, we don't update the sums list, and we just increment the repeat variable. Otherwise, we update the current element of the sums list with the sum of all elements that are smaller than the current element. We also set the repeat variable to 1, indicating that this is the first occurrence of this value.

Finally, we update the corresponding element in the ans list with the current value in sums.

Finally, the function returns the ans list."""
