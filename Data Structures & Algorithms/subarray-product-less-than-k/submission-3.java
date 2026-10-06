class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        // sliding window with two pointers with left and right
        // that will move around based on product being over k or not
        // if product is over k, move left to the right until it isn't
        // other cases, loop over right
        // counter formula : right - left + 1

        int result = 0;
        int product = 1;
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            product *= nums[right];

            while (left <= right && product >= k) {
                product /= nums[left];
                left++;
            }

            result += right - left + 1;
        }

        return result;
    }
}