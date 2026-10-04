class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;

        this.reverse(nums, 0, n - 1);
        this.reverse(nums, 0, k - 1);
        this.reverse(nums, k, n - 1);
    }

    private void reverse(int[] nums, int l, int r) {
        while (l < r) {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l += 1;
            r -= 1;
        }
    }
}


// [1,2,3,4,5,6,7,8] => // [5,6,7,8,1,2,3,4]
// [8,7,6,5,4,3,2,1]
// [5,6,7,8,4,3,2,1]
// [5,6,7,8,1,2,3,4]