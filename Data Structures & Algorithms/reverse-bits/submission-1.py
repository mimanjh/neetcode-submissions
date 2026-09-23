class Solution:
    def reverseBits(self, n: int) -> int:
        # go through n to build a string to reverse
        # go through reversed string to get integer
        nString = ""
        for i in range(32):
            if n & (1 << i):
                nString += "1"
            else:
                nString += "0"
        
        res = 0
        for i, bit in enumerate(nString[::-1]):
            if bit == "1":
                res |= (1 << i)
        return res
