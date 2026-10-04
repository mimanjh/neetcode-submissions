class Solution {
    public int minSubarray(int[] nums, int p) {
        // calculate sum of nums
        // get remainder of sum / p
        // find the minimum subarray that has the sum that can produce same remainder
        int totalSum = Arrays.stream(nums).sum();
        int target = totalSum % p;

        if (target == 0) {
            return 0;
        }

        Map<Integer, Integer> sumMap = new HashMap<>();
        sumMap.put(0, -1);

        long prefix = 0;
        int minLength = nums.length;

        for (int i = 0; i < nums.length; i++) {
            prefix += nums[i];

            int current = (int) prefix % p;

            int needed = (current - target + p) % p;

            if (sumMap.containsKey(needed)) {
                minLength = Math.min(
                    minLength,
                    i - sumMap.get(needed)
                );
            }

            sumMap.put(current, i);
        }

        return minLength == nums.length ? -1 : minLength;
    }
}