class Solution():
    def lexicographicallyLargest(self, a, n):
        i, j = 0, 0
        while i < n:
            while j < n and a[j]&1 == a[i]&1:
                j += 1
            a[i:j] = sorted(a[i:j], reverse=True)
            i = j
        return a
      
"""This function takes an array a of length n as input and sorts the array in non-decreasing order according to the lexicographic order, where an element x comes before an element y if the string representation of x is lexicographically larger than the string representation of y.

The function starts by initializing two pointers i and j to 0. The first loop runs until i reaches n. The second loop runs until j reaches n or a[j] has a different parity (even or odd) than a[i]. During the second loop, if a[j] has the same parity as a[i], the loop increments j. When the second loop ends, the function sorts the subarray a[i:j] in non-increasing order and sets i to j. Finally, the function returns the sorted a.

This implementation sorts the elements of the subarray with the same parity in non-increasing order, which ensures that the resulting array is in non-decreasing order with respect to the lexicographic order.


"""
#test change