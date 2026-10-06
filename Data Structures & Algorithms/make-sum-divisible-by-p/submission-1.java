class Solution {
    public int minSubarray(int[] nums, int p) {
        // checking if any value is the same as the needed remainder of
        // sum up to that point
        // this works since we need a subarray

        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        int remainder = totalSum % p;

        if (remainder == 0) {
            return 0;
        }

        int minLength = nums.length;
        int prefixSum = 0;
        Map<Integer, Integer> remainders = new HashMap<>();
        remainders.put(0, -1);

        for (int i = 0; i < nums.length; i++) {
            prefixSum += nums[i];

            int currentRemainder = prefixSum % p;

            int needed = (currentRemainder - remainder + p) % p; //adding p here as it may become negative.

            if (remainders.containsKey(needed)) {
                minLength = Math.min(
                    minLength,
                    i - remainders.get(needed)
                );
            }

            remainders.put(currentRemainder, i);
        }
        
        return minLength == nums.length ? -1 : minLength;
    }
}