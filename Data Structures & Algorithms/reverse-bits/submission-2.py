class Solution:
    def reverseBits(self, n: int) -> int:
        # initialize res
        # insert n's right most value to res from the left
        # shift res to the left to make space
        # insert n's last value
        # pop n's last valuep by shifting to right
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res