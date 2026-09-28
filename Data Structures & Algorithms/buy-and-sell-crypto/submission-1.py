class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = 100
        maxProfit = 0

        for x in prices:
            lowestPrice = min(lowestPrice, x)
            maxProfit = max(maxProfit, x - lowestPrice)
        return maxProfit