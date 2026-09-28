class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start from beginning
        # store the maximum difference of b - a
        # return the value
        n = len(prices)
        diff = 0

        for i in range(n-1):
            for j in range(i+1, n):
                calc = prices[j] - prices[i]
                diff = max(diff, calc)

        return diff