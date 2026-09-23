class Solution:
    def rob(self, nums: List[int]) -> int:
        # need to dynamically calculate sum of houses not nearing each other
        # max will be previous value or previous previous value + current        
        prev = 0
        curr = 0
        for x in nums:
            tmp = curr
            curr = max(prev + x, curr)
            prev = tmp
        
        return curr
