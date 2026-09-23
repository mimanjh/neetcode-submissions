class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # go through each i and j to check if nums[i] + nums[j] == target and i != j
        # return [i, j] if it matches

        for i, n in enumerate(nums):
            for j, n in enumerate(nums):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]