class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        this.backtrack(nums, current, result);
        // backtracking
        return result;
    }

    private void backtrack(
        int[] nums,
        List<Integer> current,
        List<List<Integer>> result
    ) {
        // default case
        if (current.size() == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int num : nums) {
            // don't use the same number twice
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
