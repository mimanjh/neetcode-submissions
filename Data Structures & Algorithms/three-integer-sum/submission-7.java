class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;

        // for loop with additional two pointers
        // sort for appropriate l and r shift
        // if two consecutive values on left are same, increment it twice
        Arrays.sort(nums);

        for (int i = 0; i < n; i++) {          
            int l = i + 1;
            int r = n - 1;
            int val1 = nums[i];

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            while (l < r) {
                int val2 = nums[l];
                int val3 = nums[r];

                int tempSum = val1 + val2 + val3;

                if (tempSum == 0) {
                    List<Integer> arr = new ArrayList<>();
                    arr.add(val1);
                    arr.add(val2);
                    arr.add(val3);

                    result.add(arr);
                }
                
                if (tempSum > 0) {
                    r -= 1;
                }
                else if (tempSum < 0) {
                    l += 1;
                }
                else {
                    l += 1;
                    r -= 1;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l += 1;
                    }
                    while (l < r && nums[r] == nums[r + 1]) {
                        r -= 1;
                    }
                }
            }
        };


        return result;
    }
}
