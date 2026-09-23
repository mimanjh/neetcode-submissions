class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for x in nums:
            tmp = rob2
            rob2 = max(x + rob1, rob2)
            rob1 = tmp
        
        return rob2