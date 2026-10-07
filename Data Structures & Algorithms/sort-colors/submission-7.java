class Solution {
    public void sortColors(int[] nums) {
        int[] colors = new int[3];

        for (int num : nums) {
            colors[num] += 1;
        }

        int numsIndex = 0;
        int colorCount = 0;
        for (int i = 0; i < 3; i++) {
            colorCount = colors[i];
            while (colorCount > 0) {
                nums[numsIndex] = i;
                numsIndex += 1;
                colorCount -= 1;
            }
        }
    }
}