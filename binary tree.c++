class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []

        for pile in piles:
            heapq.heappush(max_heap, -pile)

        while k != 0:
            stone = heapq.heappop(max_heap)
            stone = math.ceil(stone * -1 / 2)
            heapq.heappush(max_heap, -stone)
            k -= 1

        return -sum(max_heap)
