class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        calculated = [0] * (n + 1)
        calculated[1], calculated[2] = 1, 2

        for i in range(3, n + 1):
            calculated[i] = calculated[i-1] + calculated[i-2]

        return calculated[n]