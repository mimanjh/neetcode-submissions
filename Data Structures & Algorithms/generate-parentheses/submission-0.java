class Solution {
    public List<String> generateParenthesis(int n) {
        // backtracking: choose - explore - undo
        // how to make a well-formed parentheses...
        // 
        List<String> result = new ArrayList<>();
        StringBuilder stack = new StringBuilder();
        int open = 0;
        int close = 0;

        backtrack(open, close, n, result, stack);

        return result;
    }

    private void backtrack(int open, int close, int n, List<String> result, StringBuilder stack) {
        // if open = close = n
        if (open == close && open == n) {
            result.add(stack.toString());
            return;
        }
        // if still has opening left
        if (open < n) {
            stack.append('(');
            backtrack(open + 1, close, n, result, stack);
            stack.deleteCharAt(stack.length() - 1);
        }
        // if close is less than opening
        if (close < open) {
            stack.append(')');
            backtrack(open, close + 1, n, result, stack);
            stack.deleteCharAt(stack.length() - 1);
        }

    }
}
