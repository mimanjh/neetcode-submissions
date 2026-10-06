class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];

        for (int num : nums) {
            count[num]++;
        }

        int index = 0;
        for (int i = 0; i < 3; i++) {
            int counter = count[i];
            while (counter > 0) {
                nums[index] = i;
                index++;
                counter--;
            }
        }
    }
}