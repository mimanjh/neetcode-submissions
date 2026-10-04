class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> h = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (h.containsKey(diff)) {
                return new int[]{h.get(diff), i};
            }
            h.put(nums[i], i);
        }

        return new int[]{};
    }
}
