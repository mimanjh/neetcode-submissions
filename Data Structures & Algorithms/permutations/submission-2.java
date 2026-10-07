class Solution {
    private int[] NUMS;
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        NUMS = nums;

        // backtracking
        this.backtrack(current, result);

        return result;
    }

    private void backtrack(
        List<Integer> current,
        List<List<Integer>> result
    ) {
        // default case
        if (NUMS.length == current.size()) {
            //add it to result as a copy since current is constantly changing
            result.add(new ArrayList<>(current));
            return;
        }

        for (int num : NUMS) {
            // since unique integers, skip if same number shows up
            if (current.contains(num)) {
                continue;
            }

            // choose
            current.add(num);
            // explore
            backtrack(current, result);
            // undo
            current.remove(current.size() - 1);
        }
    }
}
