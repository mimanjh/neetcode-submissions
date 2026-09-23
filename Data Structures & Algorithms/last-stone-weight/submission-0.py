class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        # while we have x and y stones
        # compare stone weights and destroy/subtract one appropriately

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if y > x:
                heapq.heappush(heap, x - y)

            
        return abs(heap[0]) if heap else 0

