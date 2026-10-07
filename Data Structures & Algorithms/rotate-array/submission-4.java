class Solution {
    public void rotate(int[] nums, int k) {
        int l = 0;
        int r = nums.length;

        k %= r;
        swap(nums, l, r - 1);
        swap(nums, l, k - 1);
        swap(nums, k, r - 1);
    }

    private void swap(int[] nums, int l, int r) {
        while (l < r) {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }
}