class Solution {
    public int maxProfit(int[] prices) {
        // array to store maximum profit for each transaction and its index
        int maxProfit = 0;
        int lowestPrice = 100;

        for (int i = 0; i < prices.length; i++) {
            int price = prices[i];
            lowestPrice = Math.min(lowestPrice, price);
            maxProfit = Math.max(maxProfit, price - lowestPrice);
        }
        return maxProfit;
    }
}

// maxProfit = maxPrice - minPrice