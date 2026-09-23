class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                hashMap[i] = nums[i] + nums[j]
                if hashMap[i] == target:
                    return [i, j]