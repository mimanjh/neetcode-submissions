class Solution {
    public void sortColors(int[] nums) {
        // count the number of 0s, 1s, and 2s and store them in a map
        // loop through the map to just update the values appropriately

        int[] count = new int[3];

        for (int num : nums) {
            count[num]++;
        }

        int index = 0;
        for (int i = 0; i < 3; i++) {
            while (count[i]-- > 0) {
                nums[index++] = i;
            }
        }
    }
}