class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurrences = {}

        for num in nums:
            if num in occurrences:
                return True
            occurrences[num] = 1
        
        return False