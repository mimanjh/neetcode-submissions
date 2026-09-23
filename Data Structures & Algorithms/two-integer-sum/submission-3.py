class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # instead of going through both i and j, range it so that it already doesn't have i == j sitautions
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]