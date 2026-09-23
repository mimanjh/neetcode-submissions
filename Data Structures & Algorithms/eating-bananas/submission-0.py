class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        res = high = max(piles)
        

        while low <= high:
            k = (low + high) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        return res