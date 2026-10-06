class Solution {
    public int minSubarray(int[] nums, int p) {
        // what we're really looking for is if the remainders of subarrays are the same as the total remainder
        // store remainder in hashmap for look up
        // go through each values and save its prefix
        // calculate remainder to see if it's the same as target
        // formula : (currentRemainder - targetRemainder + p) % p

        int totalSum = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            totalSum += nums[i];
        }
        int targetRemainder = totalSum % p;

        if (targetRemainder == 0) {
            return 0;
        }

        Map<Integer, Integer> remaindersMap = new HashMap<>();
        remaindersMap.put(0, -1); // to incorporate the first two subarrays as answer

        int prefixSum = 0;
        int minLength = nums.length;
        for (int i = 0; i < n; i++) {
            prefixSum += nums[i];

            int currentRemainder = prefixSum % p;

            int neededRemainder = (currentRemainder - targetRemainder + p) % p;

            if (remaindersMap.containsKey(neededRemainder)) {
                minLength = Math.min(
                    minLength,
                    i - remaindersMap.get(neededRemainder)
                );
            }

            remaindersMap.put(currentRemainder, i);
        }

        return minLength == n ? -1 : minLength;
    }
}