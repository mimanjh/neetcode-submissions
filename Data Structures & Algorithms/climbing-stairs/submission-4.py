class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        c = [1, 2]
        i = 2
        while i < n:
            tmp = c[1]
            c[1] = c[0] + c[1]
            c[0] = tmp
            i += 1
        
        return c[1]