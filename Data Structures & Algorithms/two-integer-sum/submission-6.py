class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # checking if difference exists in a map

        diffMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if num in diffMap:
                return [diffMap[num], i]
            diffMap[diff] = i
        
        return []