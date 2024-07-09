class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for _ in range(k):
            current = -heapq.heappop(heap)
            current -= current // 2
            heapq.heappush(heap, -current)
        
        return -sum(heap)