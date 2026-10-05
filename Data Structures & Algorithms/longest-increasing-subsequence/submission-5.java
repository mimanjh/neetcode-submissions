class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        List<Integer> LIS = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            LIS.add(1);
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] < nums[j]) {
                    LIS.set(i, Math.max(
                        LIS.get(i), 1 + LIS.get(j)
                    ));
                }
            }
        }

        return Collections.max(LIS);
    }
}
