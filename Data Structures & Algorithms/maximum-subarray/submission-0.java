class Solution {
    public int maxSubArray(int[] nums) {
        // key idea is that
        // if the sum is less than zero, it's just better to
        // start the sum from 0 again

        int maxSum = nums[0];
        int currentSum = 0;

        for (int num : nums) {
            if (currentSum < 0) {
                currentSum = 0;
            }

            currentSum += num;
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
