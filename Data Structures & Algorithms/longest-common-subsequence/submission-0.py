class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dynamically retract characters and save previous versions as cache to save time and space
        # cache should be a hashmap to keep track
        l1 = len(text1)
        l2 = len(text2)
        def memo(i, j, cache):
            if i == l1 or j == l2:
                return 0
            if cache[(i, j)] > 0:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + memo(i + 1, j + 1, cache)
            else:
                cache[(i, j)] = max(memo(i + 1, j, cache), memo(i, j + 1, cache))

            return cache[(i, j)]
        cache = {}
        for i in range(len(text1)):
            for j in range(len(text2)):
                cache[(i, j)] = 0

        return memo(0, 0, cache)

            