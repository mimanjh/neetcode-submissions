class Solution {
    public int lengthOfLongestSubstring(String s) {
        // sliding window with two pointer
        // hashset to keep track of characters in window
        // keep track of maximum length of characters in hashset
        // if hashset doesn't have r, move r to the next level
        // if it does, move l to the next level until no duplicates exist in hashset
        int l = 0;
        int n = s.length();
        Set<Character> characters = new HashSet<>();
        int maxLength = 0;
        for (int r = 0; r < n; r++) {
            while (characters.contains(s.charAt(r))) {
                characters.remove(s.charAt(l));
                l++;
            }
            characters.add(s.charAt(r));
            maxLength = Math.max(maxLength, r - l + 1);
        }

        return maxLength;
    }
}
