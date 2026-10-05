class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int count = 0;

        // sliding window with two pointers that increase/decrease by product
        // if product is greater than k, shift left pointer to the right until product is less than k

        int product = 1;
        int left = 0;

        if (k <= 1) {
            return 0;
        }

        for (int right = 0; right < nums.length; right++) {
            product *= nums[right];
            while (product >= k) {
                product /= nums[left];
                left++;
            }
            count += right - left + 1;
        }

        return count;
    }
}