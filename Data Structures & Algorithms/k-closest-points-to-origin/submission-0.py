class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # use max heap
        # iterate each and only keep k amount
        # save the distance and coordinates
        # go through the heap and retrieve just the coordinates to return

        for x, y in points:
            d = -(x**2 + y**2)
            heapq.heappush(heap, [d, x, y])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            d, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res