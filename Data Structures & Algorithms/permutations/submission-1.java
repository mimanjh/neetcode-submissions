class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        // backtracking
        this.backtrack(nums, current, result);

        return result;
    }

    private void backtrack(
        int[] nums,
        List<Integer> current,
        List<List<Integer>> result
    ) {
        // default case
        if (nums.length == current.size()) {
            //add it to result as a copy since current is constantly changing
            result.add(new ArrayList<>(current));
            return;
        }

        for (int num : nums) {
            // since unique integers, skip if same number shows up
            if (current.contains(num)) {
                continue;
            }

            // choose
            current.add(num);
            // explore
            backtrack(nums, current, result);
            // undo
            current.remove(current.size() - 1);
        }
    }
}
