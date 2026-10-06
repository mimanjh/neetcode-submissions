class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            int l = i + 1;
            int r = nums.length - 1;

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int firstVal = nums[i];
            while (l < r) {
                int secondVal = nums[l];
                int thirdVal = nums[r];

                int threeSum = firstVal + secondVal + thirdVal;
                if (threeSum == 0) {
                    result.add(new ArrayList<>(List.of(firstVal, secondVal, thirdVal)));
                }

                if (threeSum > 0) {
                    r--;
                }
                else if (threeSum < 0) {
                    l++;
                }
                else {
                    l++;
                    r--;

                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                    while (l < r && nums[r] == nums[r + 1]) {
                        r--;
                    }
                }
            }
        }

        return result;
    }
}
