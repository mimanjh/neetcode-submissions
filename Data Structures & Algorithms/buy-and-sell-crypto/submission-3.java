class Solution {
    public int maxProfit(int[] prices) {
        int lowestPrice = 100;
        int maxProfit = 0;

        for (int i = 0; i < prices.length; i++) {
            lowestPrice = Math.min(lowestPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - lowestPrice);
        }

        return maxProfit;
    }
}

// lowest buy
// highest sell
// for loop => find the lowest
// current - lowest => max
