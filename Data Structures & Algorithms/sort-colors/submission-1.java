class Solution {
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    };

    public void sortColors(int[] nums) {
        // three pointer
        // low point to gather 0s
        // mid point to iterate from beginning to end, organizing 0s and 2s
        // high point to gather 2s
        int low = 0;
        int mid = 0;
        int high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                this.swap(nums, mid, low);
                low += 1;
                mid += 1;
            }
            else if (nums[mid] == 2) {
                this.swap(nums, mid, high);
                high -= 1;
            }
            else {
                mid += 1;
            }
        }
    }
}