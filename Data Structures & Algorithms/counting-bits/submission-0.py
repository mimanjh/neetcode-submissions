class Solution:
    def countBits(self, n: int) -> List[int]:
        # repetitive pattern seen on each offset of 2 powers
        # store them and update the result dynamically using saved data
        dp = [0] * (n + 1) # n + 1 since 0 is included
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp