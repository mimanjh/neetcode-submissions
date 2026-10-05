class Solution {
    public int lengthOfLIS(int[] nums) {
        // loop backwards and then forward like i-- and j= i+1 j++
        // store maximum increasing subsequence in hashmap
        // return maximum in hashmap
        int n = nums.length;
        int[] LIS = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                
                if (nums[i] < nums[j]) {
                    LIS[i] = Math.max(LIS[i], 1 + LIS[j]);
                }                
            }
        }

        return Arrays.stream(LIS).max().getAsInt() + 1; // add 1 here since all can at least form a subsequence containing itself.
    }
}


// 9,1,4,2,3,3,7

// [7] = 1
// [3, 7] = 2
// 3, 3, 7 = x
// 2, 3, 7 = 3
// 1, 2, 3, 7 = 4