class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dfs with memoization on saving preexisting changes
        # loop through each words separately,
        # if they match, proceed them both at the same time
        # if they don't, compare each advances and keep the minimum
        # store the values in hashmap, if it exists return that instead

        m = len(word1)
        n = len(word2)
        advanceHistory = {} # [(i, j)]
        
        def dfs(i: int, j: int):
            # base case
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in advanceHistory:
                return advanceHistory[(i, j)]

            if word1[i] == word2[j]:
                advanceHistory[(i, j)] = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                res = min(res, dfs(i + 1, j + 1))
                advanceHistory[(i, j)] = res + 1
            return advanceHistory[(i, j)]

        return dfs(0, 0)