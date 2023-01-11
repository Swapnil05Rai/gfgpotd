
class Solution:
    def minIncrements(self, arr, N): 
        unique_values = set()
        increments = 0
        for i in range(len(arr)):
            while arr[i] in unique_values:
                arr[i] += 1
                increments += 1
            unique_values.add(arr[i])
        return increments


"""The function  minIncrements takes in an array arr as input. It initializes an empty set unique_values to store the unique elements of the array, and a variable increments to keep track of the number of increments made.

The function then uses a for loop to iterate through each element of the array. Inside the for loop, it uses a while loop to repeatedly increment the current element until it is not already in the set unique_values. Everytime we increment current element, we also increment a counter increments by 1.

Once the current element is a unique value (not found in set), it is added to the set of unique values.

Finally, after iterating through all the elements in the array, the function returns the total number of increments made as the final answer.

The example input arr[] = {1, 2, 2} will gives us the output 1 as we only need to increment last element of array i.e 2 to make it unique, hence only 1 increment required to make array unique.



"""
