import heapq

class Solution:
    def minimizeSum(self, N, arr):
        pq = []
        for i in range(N):
            heapq.heappush(pq, arr[i])

        total_sum = 0
        while len(pq) > 1:
            a = heapq.heappop(pq)
            b = heapq.heappop(pq)
            total_sum += a + b
            heapq.heappush(pq, a + b)

        return total_sum
"""The strategy is as follows:

Always select the two smallest elements from the list, sum them, and add the sum back to the list.
Repeat step 1 until the list has only one element left, which will be the minimum sum.
The explanation for the above strategy is that by always selecting the two smallest elements and summing them,
you are choosing the pair that has the minimum possible sum, and this will make the overall sum of all the pairs as small as possible.

Both provided implementation uses a priority queue (heap) to sort elements and get the smallest element, and they both have an O(n log n) time complexity."""
